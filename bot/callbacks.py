from aiogram.filters.callback_data import CallbackData


class SendSelfiCallback(CallbackData, prefix='send_selfi'):
    pass


class SendHighSchoolPhotoCallback(
    CallbackData,
    prefix='send_highschool_photo',
):
    pass


class DescribeChatGPTCallback(
    CallbackData,
    prefix='describe_chatgpt',
):
    pass


class DescribeSQLNoSQLCallback(
    CallbackData,
    prefix='describe_sql_nosql',
):
    pass


class DescribeLoveStory(
    CallbackData,
    prefix='describe_love_story',
):
    pass
