from asyncio import sleep
from .. import loader, utils

def register(cb):
	cb(ЗаёбушкаMod())
	
class ЗаёбушкаMod(loader.Module):
	"""Заебет любого"""
	strings = {'name': 'Заёбушка'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	def get_args(message):
    """Get arguments from message (str or Message), return list of arguments"""
    try:
        message = message.message
    except AttributeError:
        pass
    if not message:
        return False
    message = message.split(sep='_',maxsplit=1)
    if len(message) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message  # Cannot split, let's assume that it's just one long message
    return list(filter(lambda x: len(x) > 0, split))
		
	async def заебуcmd(self, message):
		""".заебу <колличество> <реплай на того, кого заебать>"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("<b>А кого заёбывать-то?</b>")
			return
		id = reply.sender_id
		args = utils.get_args(message)
		count = 50
		if args:
			if args[0].isdigit():
				if int(args[0]) < 0:
					count = 50
				else:
					count = int(args[0])
		txt = '<a href="tg://user?id={}">{}</a>'
		await message.edit(txt.format(id, "Я тебя заебу!"))
		for _ in range(count):
			await sleep(0.3)
			msg = await message.client.send_message(message.to_id, txt.format(id, "Заёбушка:3"), reply_to=message)
			if not msg.is_reply:
				await msg.edit("<b>Остановлено!</b>")
				break
			await sleep(0.3)
			await msg.delete()

	async def zbcmd(self, message):
		""".заебу <колличество> <реплай на того, кого заебать>"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("<b>А кого заёбывать-то?</b>")
			return
		id = reply.sender_id
		args = get_args(message)
		count = 5
		if args:
			if args[0].isdigit():
				if int(args[0]) < 0:
					count = 5
				else:
					count = int(args[0])
		txt = '<a href="tg://user?id={}">{}</a>'
		await message.edit(txt.format(id, "Я тебя заебу!"))
		for _ in range(count):
			await sleep(0.3)
			msg = await message.client.send_message(message.to_id, txt.format(id, "Заёбушка:3"), reply_to=message)
			if not msg.is_reply:
				await msg.edit("<b>Остановлено!</b>")
				break
			await sleep(0.3)
			await msg.delete()				
			
