import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "22420997"))
    API_HASH = os.environ.get("API_HASH", "d7fbe2036e9ed2a1468fad5a5584a255")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "7170426058")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://chaiwala:autqio99wvMJEr0l@cluster0.nupdo.mongodb.net/chai?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "chai")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002247666039"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "nothing")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
