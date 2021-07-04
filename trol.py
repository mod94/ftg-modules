from .. import loader, utils

import logging
import random


logger = logging.getLogger(__name__)


@loader.tds
class TrolMod(loader.Module):
    """Shouts at people"""
    strings = {"name": "trol"}

    @loader.unrestricted
    async def trolcmd(self, message):
        """Use when angry"""
        # TODO localisation?
        adjectives_start = ["сучий", "жирный", "ебаный", "обосраный", "глупый", "безмозглый"]
        adjectives_mid = ["мелкий", "ушибленый"]
        nouns = ["псина", "свинья", "педофил", "недомальчик", "униженый", "обиженый", "жополиз", "яйцеглот",
                 "ХУЙ", "залупа", "далюаеб", "мамкаеб", "пиздолиз", "хуесос"]
        starts = ["Слыш ты", "Ты", "Завали ебало ты", "Cлушай сюда ты",
                  "Да что блядь с тобой, ты"]
        ends = ["!!!!", "!", ""]
        start = random.choice(starts)
        adjective_start = random.choice(adjectives_start)
        adjective_mid = random.choice(adjectives_mid)
        noun = random.choice(nouns)
        end = random.choice(ends)
        insult = start + " " + adjective_start + " " + adjective_mid + (" " if adjective_mid else "") + noun + end
        logger.debug(insult)
        await utils.answer(message, insult)
