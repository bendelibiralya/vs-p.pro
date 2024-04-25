import discord
import os
import requests
import random
from bot_logic import *
from discord.ext import commands
from dtoken import token

#yetkiler
intents = discord.Intents.default()
intents.message_content = True
#normalde yazının başında yazan $
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def parola(ctx, pass_lenght = 8):
    password = gen_pass(pass_lenght)
    await ctx.send(password)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    with open("images\M2L1-T2-2_ksnyah.png", 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send("al sana mem!")
    await ctx.send(file=picture)

@bot.command()
async def random_mem(ctx):
    img_list = os.listdir('images')
    img_name = random.choice(img_list)
    with open(f'images/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send("al sana mem!")
    await ctx.send(file=picture)

@bot.command()
async def kedy(ctx):
    foti_list = os.listdir("kitties")
    foti_name = random.choice(foti_list)
    with open(f'kitties/{foti_name}', "rb") as f:
        pickitty = discord.File(f)
    await ctx.send("KEDY!")
    await ctx.send(file=pickitty)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('köpke')
async def köpke(ctx):
    '''dog komutunu çağırdığımızda, program get_dog_image_url fonksiyonunu çağırır.'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run(token)