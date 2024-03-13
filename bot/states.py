from aiogram.fsm.state import (
    State,
    StatesGroup,
)


class BotStates(StatesGroup):
    choose_photo_type = State()
    send_selfie = State()
    send_high_school_photo = State()
    my_hobbies = State()
    describe_me = State()
    describe_chatgpt = State()
    describe_sql_nosql = State()
    describe_love_story = State()
