# fake ping
# Subscribe to channel @modwini
import random
import logging
from .. import loader, utils
from random import randint, choice

logger = logging.getLogger(__name__)

def register(cb):
    cb(pinj())


class pinj(loader.Module):
    """Fake ping"""
    strings = {'name': 'pinj by @modwini'}

    async def pinjcmd(self, message):
        """use .ping <numbers>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit('<b>no argument after command-_- </b>')
            return
        else:
            pinj = ("⏱" + "<b> Telegram ping:  </b>" + f"<code>{text}</code>" + "<b> ms</b>" + " <b> \n😎 Uptime: 10:29:59 \n</b>")

            await message.edit(pinj)