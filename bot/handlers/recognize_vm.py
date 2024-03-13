import socket
from typing import BinaryIO
from random import choice
from aiogram import F
from aiogram.types import ContentType as CT
from aiogram import types
from aiogram.fsm.context import FSMContext

import config
from bot.constants import (
    CANT_RECOGNIZE_VOICE_MESSAGES,
    COMMANDS_DESCRIPTION,
    WAIT_RECOGNIZE_VOICE_MESSAGES,
)
from bot.handlers.hobbies import my_hobbies
from bot.handlers.photos import my_photos
from bot.handlers.voices import describe_me
from bot.instances import dispatcher, bot
from bot.utils import best_key_by_value


handlers_by_commands = {
    '/my_photos': my_photos,
    '/my_hobbies': my_hobbies,
    '/describe_me': describe_me,
}


def tcp_echo_client(audio: BinaryIO):
    addr = config.STT_SOCKET_HOST, config.STT_SOCKET_PORT
    channel_size = config.STT_SOCKET_CH_SIZE

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(addr)

    data = audio.read(channel_size)
    while data:
        tcp_socket.send(data)
        data = audio.read(channel_size)

    tcp_socket.shutdown(socket.SHUT_WR)
    resp = tcp_socket.recv(channel_size).decode('utf-8')
    tcp_socket.close()
    return resp


@dispatcher.message(F.content_type.in_([CT.VOICE]))
async def recognize(
    message: types.Message,
    state: FSMContext,
) -> None:
    MATCH_LIMIT = 0.5

    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    result: BinaryIO = await bot.download_file(file_path)
    await message.answer(
        text=(
            choice(WAIT_RECOGNIZE_VOICE_MESSAGES)
        )
    )
    text = tcp_echo_client(result)  # TODO make awaitable
    matched_command = best_key_by_value(
        COMMANDS_DESCRIPTION,
        text,
        MATCH_LIMIT,
    )
    if matched_command:
        handler_foo = handlers_by_commands.get(matched_command)
        if handler_foo:
            await handler_foo(message, state)
            return

    await message.answer(
        text=(
            choice(CANT_RECOGNIZE_VOICE_MESSAGES)
        )
    )
