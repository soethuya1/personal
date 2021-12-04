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

elif 'ouo.press' in link:
        return ouo(link)
elif 'ouo.io' in link:
        return ouo(link)

def ouo(url: str) -> str:
    """ Bypass OuO
    Based on https://github.com/zevtyardt/lk21
    """
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_ouo(url)

    sendMessage(<code>{dl_url}</code>)

DIRECT_HANDLER = CommandHandler(BotCommands.DirectCommand, direct, 
                                                  filters=CustomFilters.owner_filter | CustomFilters.authorized_user, run_async=True)

dispatcher.add_handler(DIRECT_HANDLER)
