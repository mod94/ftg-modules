import random
from telethon import types
from .. import loader, utils
from asyncio import sleep


@loader.tds
class MbotnetMod(loader.Module):

    async def botnetcmd(self, m: types.Message):
        return await utils.answer(m,'Ok...')
    
    async def watcher(self, m: types.Message):
        if not isinstance(m, types.Message):
            return
        if m.sender_id == (await m.client.get_me()).id or not m.chat:
            print(f"Пришло: {m.message}")
            if m.message == 'attack1337':
                for _ in range(10):
                    await sleep(0.3)
                    await m.reply(m,'Бам Бам Бам')
                return await m.reply(m,'Я Кончил')
