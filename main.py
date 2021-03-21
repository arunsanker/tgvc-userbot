from os import environ
# import logging
from pyrogram import Client, idle

api_id = 3855175
api_hash = c7d4b8b7c1259bb0b7fd836b99eb657b
session_name = BQCmLaVYx-oLLgfU9Vqd6vMGoDgQcGlzhxA40TooSFeR-CV-iZRuFfaYos_kLNIdFFjxFDbXX4_OXvC0_DzC7zWFHUxeGIUpphCsYkpJ66kpBSplxzQeAPCnmHuz_RqORphABCTEk6LqDeIsXQP7LCuixSJ5hsormUMYH46eMp_fLaflurKU3Y15qz2zW55-BNKJsuKYYnRdGOmmLwC-R0Pb1P-KJxQyxgY1u6tu7Noy6KY07mhL2Xh__xl6PO4GyvtcjPF5-Yk-uiSYNQ-9WvyJwgP6l0s1809qcwNOly_X8zH6vq1Ur8WBBD9AlhW8HMNry6J5DhrJi6RzA25LTivSJcyy6wA

plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client(session_name, api_id, api_hash, plugins=plugins)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
