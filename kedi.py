import discord
import os
import random
from dtoken import token
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
#normalde yazının başında yazan $
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def kedy(ctx):
    foti_list = os.listdir("kitties")
    foti_name = random.choice(foti_list)
    with open(f'kitties/{foti_name}', "rb") as f:
        pickitty = discord.File(f)
    await ctx.send("KEDY!")
    await ctx.send(file=pickitty)

@bot.command()
async def uzgunkedy(ctx):
    uzgunler_list = os.listdir("uzgunkedyler")
    uzgunler_name = random.choice(uzgunler_list)
    with open(f'uzgunkedyler/{uzgunler_name}','rb') as f:
        uzgunfoti = discord.File(f)
    await ctx.send("SAD!")
    await ctx.send(file=uzgunfoti)

bot.run(token)