from telethon import TelegramClient,events

client=TelegramClient('bot_sission', api_id= 25046160,api_hash='a383f8a163dd0b1aaa6ffc6dc14529d8' )

@client.on(events.NewMessage(pattern=r'/start'))
async def start(event):
    await client.send_message(entity=event.chat_id,message='Hello:123')

client.start()
client.run_until_disconnected()