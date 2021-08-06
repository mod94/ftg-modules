from .. import loader, utils

import logging
import random


logger = logging.getLogger(__name__)


@loader.tds
class CyganMod(loader.Module):
    """Shouts at people"""
    strings = {"name": "trol"}

    @loader.unrestricted
    async def cygancmd(self, message):
        """Use when angry"""
        # TODO localisation?       
        insult = "☑️ конь спижен"
        logger.debug(insult)
        await utils.answer(message, insult)
