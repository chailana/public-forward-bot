import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQFWHgUAkKYKqHTzQpzU7Ea4H0ct7aaDCCkAU9oIBgan6-s4YC_PylsYdMK4t46CY4c1CxuL4kfC2DxO7q4SmTOvW5TaHlDh7Ucq9P-MeqkrLCYHDqUjS0Vi8cgdM7UNObIUVIeKfi8knCZIeEI_bEm9KjdHajVfCDA7gci8kDAhTuV2tENG_GOT3NR9naeo551ZT2HUpgjM4Pl3dkKTPIzAHTx3AbnW_nFqfMC9q--8N-iSm3BRq7n4D4MIS5f-Mydu57ZdWODNESD28T1OotG9hCIzGqeCMe345jU5JdRq_CBujDuMrj3QdzHJznzIs5YMCPdgNxWwWpTHH6EMdwrv0S5W3gAAAAGrZATKAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
