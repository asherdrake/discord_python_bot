import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio
from reminder_cog import reminder_cog

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = "?", description="biladidod", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print(bot.get_cog('reminder_cog'))

async def load_cogs():
    await bot.load_extension("reminder_cog")

asyncio.run(load_cogs())
bot.run(os.getenv('TOKEN'))


