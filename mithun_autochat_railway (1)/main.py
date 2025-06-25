import asyncio
from telethon import TelegramClient, events
from groq import Groq
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE, GROQ_API_KEY
from keep_alive import keep_alive

client = TelegramClient("session", TELEGRAM_API_ID, TELEGRAM_API_HASH)
groq_client = Groq(api_key=GROQ_API_KEY)
active_users = {}

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    sender_id = sender.id
    if sender_id in active_users and active_users[sender_id]["active"]:
        return
    prompt = event.raw_text
    completion = groq_client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-70b-8192"
    )
    await event.respond(completion.choices[0].message.content)
    print(f"Replied to {sender_id}")

async def main():
    await client.start(phone=TELEGRAM_PHONE)
    print("Bot is running 24/7...")
    await client.run_until_disconnected()

keep_alive()
asyncio.run(main())