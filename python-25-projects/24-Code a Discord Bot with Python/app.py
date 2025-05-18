import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set command prefix and intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# On ready
@bot.event
async def on_ready():
    print(f'✅ Bot is ready. Logged in as {bot.user}')

# Simple hello command
@bot.command()
async def hello(ctx):
    await ctx.send(f'👋 Hello, {ctx.author.name}!')

# Run the bot
bot.run(TOKEN)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I’m alive!")

