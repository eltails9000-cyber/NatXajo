import os

class Config:
    TOKEN = os.getenv("DISCORD_TOKEN")

    API_URL = os.getenv("API_URL")
    API_KEY = os.getenv("ROBLOX_API_KEY")

    OWNER_ID = 1042929958286266540


config = Config()
