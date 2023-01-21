import asyncio
import discord
from dotenv import load_dotenv
import os
from discord.ext.commands import Bot
from fastapi import FastAPI


load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")


intents = discord.Intents.all()
bot = Bot(command_prefix='!', help_command=None, intents=intents)


@bot.event
async def on_message(message):
    # do not reply to self
    if message.author == bot.user:
        return

    # do not reply ot other bots
    if message.author.bot:
        return

    # get the message content
    msg = message.content.lower()

    # reply to the ping message
    if "!ping" in msg:
        await message.reply("Pong!", mention_author=False)

    
app = FastAPI()
@app.get("/")
def main():
    return "The bot is alive and well"

# run the bot as a FastAPI async function
@app.on_event("startup")
async def run():
    """
    To run the bot as a FastAPI async function
    """
    try:
        asyncio.create_task(bot.start(TOKEN))

    except:
        await bot.logout()

        
