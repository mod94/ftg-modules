from telethon import events
import time

"""Command: .spamprn <number> НЕ ПРОБЫВАТЬ НА СВОЕМ АККАУНТЕ

telethon.errors.rpcerrorlist.FloodWaitError: A wait of 280 seconds is required"""

@borg.on(events.NewMessage(pattern=r"\.spamprn (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    for i in range(int(input_str)):
        m = await event.respond("https://blyadun.com/uploads/posts/2017-12-11-21/d30145d84a68766d5b8b65155b4e7c75_206279_07big.jpg")
    if "|" in input_str:
        counter, spam_text = input_str.split("|")
        shiiinabot = "\u2060"
        for i in range(4000):
            shiiinabot += "\u2060"
        message_text = shiiinabot + spam_text
        await event.edit(message_text)
        for i in range(int(counter)):
            time.sleep(0.3)
            await event.respond(message_text)
        await event.delete()
    else:
        await event.edit("отправь сообщение по типу `.spamprn count | spam message` и админы не увидят в недавних сообщениях" +
                         " \n Вежливо обращаюсь: @shiiinabot")
