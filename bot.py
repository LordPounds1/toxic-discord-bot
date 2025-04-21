import discord
import joblib
import os
import random

print("🔥 Бот стартует...")

TOKEN = os.getenv("DISCORD_TOKEN")

model = joblib.load("toxic_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

insults = [
    "ты что, совсем? подумай, прежде чем писать.",
    "завали хлебало, токсик.",
    "поменьше говна — побольше смысла.",
    "пиздуй с такой токсичностью отсюда.",
    "ты в баню собрался, а не в диалог.",
]

@client.event
async def on_ready():
    print(f"Бот запущен как {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions or message.content.startswith("!tox "):
        if message.content.startswith("!tox "):
            text = message.content[5:]
        else:
            text = message.content.replace(f"<@{client.user.id}>", "").replace(f"<@!{client.user.id}>", "").strip()

        X = vectorizer.transform([text])
        pred = model.predict(X)[0]

        if pred == 1:
            response = random.choice(insults)
            await message.reply(f"⚠️ {response}")
        else:
            await message.reply("👍")

try:
    client.run(TOKEN)
except Exception as e:
    print(f"❌ Ошибка запуска: {e}")
