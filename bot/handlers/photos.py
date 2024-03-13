
from aiogram import filters
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from bot import callbacks
from bot.instances import dispatcher
from bot.states import BotStates


@dispatcher.message(filters.Command('my_photos'))
async def my_photos(
    message: types.Message,
    state: FSMContext,
) -> None:
    keyboard = [
        [
            types.InlineKeyboardButton(
                text='Selfi',
                callback_data=callbacks.SendSelfiCallback().pack(),
            ),
            types.InlineKeyboardButton(
                text='From school',
                callback_data=callbacks.SendHighSchoolPhotoCallback().pack(),
            ),
        ],
    ]
    await message.answer(
        text='Choose photo type',
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=keyboard,
        ),
    )
    await state.set_state(BotStates.choose_photo_type)


@dispatcher.callback_query(callbacks.SendSelfiCallback.filter())
async def send_selfi(
    callback: types.CallbackQuery,
    state: FSMContext,
) -> None:
    photo = FSInputFile('assets/selfi.jpg')
    await callback.message.answer_photo(photo)
    await state.set_state(BotStates.send_selfie)


@dispatcher.callback_query(callbacks.SendHighSchoolPhotoCallback.filter())
async def send_highschool_photo(
    callback: types.CallbackQuery,
    state: FSMContext,
) -> None:
    photo = FSInputFile('assets/high-school.jpg')
    await callback.message.answer_photo(photo)
    await state.set_state(BotStates.send_high_school_photo)
