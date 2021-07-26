import asyncio
import telethon
from telethon.tl.types import ChannelParticipantsAdmins
from .. import loader, utils



@loader.tds
class admtagMod(loader.Module):
    """admtag"""
    strings = {"name": "admtag"}

    async def usercmd(self, message):
        """admtag"""
        args = utils.get_args_raw(message)
        await message.delete()
        if not args: return
        mentions = '<a href="tg://settings">Админы</a>, '
        counter = 0
        chat = await message.get_input_chat()
        async for x in message.client.iter_participants(chat, filter=channelParticipantsRecent):
            mentions += f'<a href="tg://user?id={x.id}">\u2060</a>'
            counter += 1
        if counter == 0: return await message.delete()
        mentions += args
        await message.respond(mentions)
