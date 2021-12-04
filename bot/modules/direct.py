import json
import math
import re
import urllib.parse
import lk21
import requests
import cfscrape


from bot.helper.telegram_helper.filters import CustomFilters
from bot import dispatcher
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage
from telegram.ext import CommandHandler  


def direct(update, context):
    if 'ouo.press' in link
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_ouo(url)
    await update.reply_text('{dl_url}')


DIRECT_HANDLER = CommandHandler(BotCommands.DirectCommand, direct, 
                                                  filters=CustomFilters.owner_filter | CustomFilters.authorized_user, run_async=True)

dispatcher.add_handler(DIRECT_HANDLER)
