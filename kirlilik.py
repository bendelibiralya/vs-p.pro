import discord
from dtoken import token
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
#normalde yazının başında yazan $
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def kirlilik(ctx):
    await ctx.send("Hangi atığın zarar verdiği hayvanları bilmek istiyorsun?")
    await ctx.send("plastik, pil, cam, metal, misina, izmarit, poset.")

@bot.command()
async def plastik(ctx):
    await ctx.send("Foklar, inekler ve deniz kaplumbağaları :(")

@bot.command()
async def pil(ctx):
    await ctx.send("Böcekler :(")

@bot.command()
async def cam(ctx):
    await ctx.send("Bütün sokak hayvanları :(")

@bot.command()
async def metal(ctx):
    await ctx.send("İnekler :(")

@bot.command()
async def misina(ctx):
    await ctx.send("Balıklar, ördekler ve kuşlar :(")

@bot.command()
async def izmarit(ctx):
    await ctx.send("Bütün sokak hayvanları :(")

@bot.command()
async def poset(ctx):
    await ctx.send("Deniz kaplumbağaları ve kuşlar :(")

bot.run(token)