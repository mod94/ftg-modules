
from .. import loader, utils
import logging
import asyncio
import random


logger = logging.getLogger(__name__)


@loader.tds
class TrolerMod(loader.Module):
    """Annoys people really effectively"""
    strings = {"name": "Spam",
               "need_spam": "<b>U wot? I need something to spam.</b>",
               "spam_urself": "<b>Go spam urself.</b>",
               "nice_number": "<b>Nice number bro.</b>",
               "much_spam": "<b>Haha, much spam.</b>"}

    async def trolercmd(self, message):
        """.spam <count> <message>"""
        use_reply = False
        args = utils.get_args(message)
        logger.debug(args)
        if len(args) == 0:
            await utils.answer(message, self.strings("need_spam", message))
            return
        if len(args) == 1:
            if message.is_reply:
                use_reply = True
            else:
                await utils.answer(message, self.strings("spam_urself", message))
                return
        count = args[0]
        spam = (await message.get_reply_message()) if use_reply else message
        spam.message = " ".join(args[1:])
        try:
            count = int(count)
        except ValueError:
            await utils.answer(message, self.strings("nice_number", message))
            return
        if count < 1:
            await utils.answer(message, self.strings("much_spam", message))
            return
        await message.delete()
        if count > 20:
            # Be kind to other people
            sleepy = 2
        else:
            sleepy = 0
        i = 0
        size = 1 if sleepy else 100
        while i < count:
            await asyncio.gather(*[message.respond(insult()) for x in range(min(count, size))])
            await asyncio.sleep(sleepy)
            i += size
        await self.allmodules.log("spam", group=message.to_id, data=spam.message + " (" + str(count) + ")")

    def insult():
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
        return insult
