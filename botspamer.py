from .. import loader, utils

import logging
import random
import time


logger = logging.getLogger(__name__)


@loader.tds
class BotspamerMod(loader.Module):
    """Shouts at people"""
    strings = {"name": "trol"}

    @loader.unrestricted
    async def Botspamercmd(self, message):
        """Use when angry"""
        
        await utils.answer(message, ".troler@youadminmybiches 30 lol")
        time.sleep(1)
        await utils.answer(message, ".troler@jrtjgrjojogr 30 lol")
        time.sleep(1)
        await utils.answer(message, ".troler@oirtuyoruiotyuorty 30 lol")
        time.sleep(1)
        await utils.answer(message, ".troler@helomamasha 30 lol")
        time.sleep(1)
        await utils.answer(message, ".troler@isnehasish 30 lol")
        time.sleep(1)
        await utils.answer(message, ".troler@lkaejgjkwsdfkghwlksdgk 30 lol")
        time.sleep(1)
        await utils.answer(message, ".troler@khalander786 30 lol")
        time.sleep(1)
        await utils.answer(message, ".troler@Alenp9 30 lol")
        time.sleep(1)
        await utils.answer(message, ".troler@Primoix 30 lol")
