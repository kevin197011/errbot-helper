import logging
from dotenv import load_dotenv
import os
import sys

sys.path.append("lib")

load_dotenv()

# vars
BASE_PATH = os.path.dirname(os.path.realpath("__file__"))

TOKEN = os.getenv("TELEGRAM_TOKEN")
# TOKEN = os.getenv("SLACK_TOKEN")


# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

# Errbot will start in text mode (console only mode) and will answer commands from there.
BACKEND = "Telegram"
# BACKEND = "SlackV3"

# BOT_EXTRA_BACKEND_DIR = (
#     f"{BASE_PATH}/.venv/lib/python3.11/site-packages/errbot/backends"
# )

# if BACKEND == "SlackV3":
#     BOT_EXTRA_BACKEND_DIR = (
#         f"{BASE_PATH}/.venv/lib/python3.11/site-packages/errbot/backends"
#     )


BOT_DATA_DIR = f"{BASE_PATH}/data"
BOT_EXTRA_PLUGIN_DIR = f"{BASE_PATH}/plugins"

BOT_LOG_FILE = f"{BASE_PATH}/errbot.log"
BOT_LOG_LEVEL = logging.INFO

BOT_ADMINS = (
    # "",
)  # Don't leave this as "@CHANGE_ME" if you connect your errbot to a chat system!!

BOT_IDENTITY = {"token": TOKEN}
