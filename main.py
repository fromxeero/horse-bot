bot
import discord
from discord.ext import commands

# intents allowing the bot to read mssgs
intents = discord.Intents.default()
intents.message_content = True 

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    # Prevent bot feedback loop
    if message.author == client.user:
        return

    # Check for phrase (not case-sensitive)
    if message.content.lower() == "i'm so hungry":
        await message.channel.send("How Hungry?")

# Replace 'TOKEN' with your bot token from the Discord Dev Portal
client.run('TOKEN')