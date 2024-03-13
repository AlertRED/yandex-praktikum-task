
from aiogram import filters
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from bot import callbacks
from bot.instances import dispatcher
from bot.states import BotStates


@dispatcher.message(filters.Command('describe_me'))
async def describe_me(
    message: types.Message,
    state: FSMContext,
) -> None:
    keyboard = [
        [
            types.InlineKeyboardButton(
                text='Что такое chatGPT',
                callback_data=callbacks.DescribeChatGPTCallback().pack(),
            ),
        ],
        [
            types.InlineKeyboardButton(
                text='SQL vs NoSQL',
                callback_data=callbacks.DescribeSQLNoSQLCallback().pack(),
            ),
        ],
        [
            types.InlineKeyboardButton(
                text='Любовная история',
                callback_data=callbacks.DescribeLoveStory().pack(),
            ),
        ],
    ]
    await message.answer(
        text='Choose photo type',
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=keyboard,
        ),
    )
    await state.set_state(BotStates.describe_me)


@dispatcher.callback_query(callbacks.DescribeChatGPTCallback.filter())
async def describe_chatgpt(
    callback: types.CallbackQuery,
    state: FSMContext,
) -> None:
    audio = FSInputFile('assets/chatgpt-is.mp3')
    await callback.message.answer_voice(audio)
    await state.set_state(BotStates.describe_chatgpt)


@dispatcher.callback_query(callbacks.DescribeSQLNoSQLCallback.filter())
async def describe_sql_nosql(
    callback: types.CallbackQuery,
    state: FSMContext,
) -> None:
    audio = FSInputFile('assets/love-story.mp3')
    await callback.message.answer_voice(audio)
    await state.set_state(BotStates.describe_sql_nosql)


@dispatcher.callback_query(callbacks.DescribeLoveStory.filter())
async def describe_love_story(
    callback: types.CallbackQuery,
    state: FSMContext,
) -> None:
    audio = FSInputFile('assets/love-story.mp3')
    await callback.message.answer_voice(audio)
    await state.set_state(BotStates.describe_love_story)
