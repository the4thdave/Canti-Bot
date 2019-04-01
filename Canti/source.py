# Canti by David Munoz

import discord
from discord.ext import commands
from discord import Game
import asyncio
import random

TOKEN = "XXXXXXXXXXXX"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="with Naota"))
    print("Tch...")
    print("{} online.".format(bot.user.name))
    print(bot.user.id)
    print("------")

@bot.command(pass_context=True,
             brief="This one's for you, Jordan.",
             description="Pen pong! Ping?")
async def ping(ctx):
    await bot.say(":ping_pong:")

@bot.command(pass_context=True,
             brief="Say hello to Canti!",
             description="Friendly greetings :)")
async def hello(ctx):
    await bot.say("Hey!")

@bot.command(pass_context=True,
             brief="A command only for Robin",
             description="Say hi to Robin, Canti.")
async def robin(ctx):
    await bot.say("<@{}> is the best! :smile:".format(387087522120859660))

@bot.command(pass_context=True,
             brief="Tch...",
             description="Robot booting up noise?")
async def wake(ctx):
    await bot.say("Tch....")

@bot.command(name="8ball",
             pass_context=True,
             brief="Answers with MAGIC",
             description="Answers a yes/no question")
async def eight_ball(ctx):
    responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
                 "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
                 "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                 "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
    await bot.say(random.choice(responses))

@bot.command(pass_context=True,
             brief="It's your song Canti!",
             description="Canti sends link to FLCL ending")
async def song(ctx):
    await bot.say("https://www.youtube.com/watch?v=XdgqDL2l0hQ")


bot.run(TOKEN)
