import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6419607127:AAF6_TA2KBiumlZJSh78aE_FXhvU1CiKxRg")

    APP_ID = int(os.environ.get("APP_ID", 25069425))

    API_HASH = os.environ.get("API_HASH", "9c58142ef6abed28808a50e3e983c39c")

