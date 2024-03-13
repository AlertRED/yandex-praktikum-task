
from aiogram import filters
from aiogram import types
from aiogram.fsm.context import FSMContext

from bot.instances import dispatcher
from bot.states import BotStates


async def my_hobbies(
    message: types.Message,
    state: FSMContext,
) -> None:
    await message.answer(
        text=(
            'Я занимаюсь бэкенд-разработкой на Python '
            'стараясь держаться SOLID и KISS. '
            'В перерывах между работой я всегда занимаюсь '
            'каким-нибудь собственным проектом или работаю на фрилансе.'
            ' Я всегда рад изучить что-то новое (язык программирования'
            ', фреймворк, технологию и т.д.).'
        )
    )
    await state.set_state(BotStates.my_hobbies)


@dispatcher.message(filters.Command('my_hobbies'))
async def my_hobbies_message(
    message: types.Message,
    state: FSMContext,
) -> None:
    await my_hobbies(message, state)
