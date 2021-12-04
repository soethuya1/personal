import json
import math
import re
import urllib.parse
import lk21
import requests
import cfscrape

from os import popen
from random import choice
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from js2py import EvalJs
from lk21.extractors.bypasser import Bypass
from base64 import standard_b64encode

from bot.helper.telegram_helper.filters import CustomFilters
from bot import dispatcher
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage
from bot.helper.ext_utils.exceptions import DirectDownloadLinkException
from telegram.ext import CommandHandler  


def direct(update, context):
    if not ouo:
        raise DirectDownloadLinkException("No links found!")
    elif 'ouo.io' in url:
        return ouo(url)
    elif 'ouo.press' in url:
        return ouo(url)
    else:
        raise DirectDownloadLinkException(f'No Direct link function found for {link}')
    

def ouo(url: str) -> str:
    """ Bypass OuO
    Based on https://github.com/zevtyardt/lk21
    """
    bypasser = lk21.Bypass()
    dirl=bypasser.bypass_ouo(url)
    return sendMessage('{dirl}')


DIRECT_HANDLER = CommandHandler(BotCommands.DirectCommand, direct, 
                                                  filters=CustomFilters.owner_filter | CustomFilters.authorized_user, run_async=True)

dispatcher.add_handler(DIRECT_HANDLER)
