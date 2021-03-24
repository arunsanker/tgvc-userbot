from os import environ
# import logging
from pyrogram import Client, idle

api_id = 2014749
api_hash = 1ca0d92db969b974c1832772b7270386
session_name = BQAVzSKs_g7OGPn0CCxidBMRYL-eZawYkz7fmWU43_76262Cc8BuOswFuAkWe2yhfvdg1IsribHlRjPY1Sz3q9uVrFoNnzwzH--foB9MFctTXOj4zbszym3bJ3oeoaWmBpNVKNXPoYZAoODDrVmm4LYdfl8hHSJj_qoQehhPiirBKlw5AM8jEaA9Oh0kzAR8C2nRkKz4PW3TkpKfd_XWLXYPdy93Ax8m9ijxClZlUjEHX-j8que1jlQ9I-C3LlLZ31F61l_PJsRiTH914lNRTKbGt9Qa14NzpJ96exJ6OaoDxXHjCJkIG1T_q_kz8WVW3eCDuJK5Dz_CIUoNl5ZHiGJ1RuvEfgA

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
