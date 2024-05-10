from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "25971977")
APP_HASH = os.environ.get("APP_HASH", "10041628a847c909b20400706c00ae36")
SESSION = os.environ.get("1BJWap1sBu26BBYobbGz4KNPizKidRehXu8Vuw0SLyB0ADB9eZwZGulWgYgt_j9SQt6iz62RfdSPr_B4ALSTDAv_ylguTsI7r07OpuWkdUqQmM1QHy0WAICOySXpQgEB2W5f1ZZvNUudIAlqxOta2TTZtovuSbifF7QoKjfVVYEIGUeTreNYJye6ORlDtj_SE2F9bJAQ_gUmNtqKvvEO5NqhsyPMsVLcdHlG56zD9fdeN_k67I6_3bwn9sgr486XLYJKDK4dxK7XsM8X_PDY6_6C-Y40eiwpx6yB9vTuZAUtil_-EjTAymK_Qe-OizGw0AF9mK3VDGSmGaiOwYWdoiY459unnZW8=")
ha313so = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
ha313so.start()
