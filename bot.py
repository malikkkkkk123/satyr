import discord
from discord.ext import commands
from main import *
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')



@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
        await ctx.send(f'bye!')
        
@bot.command()
async def password(ctx, count_password = 10):
    await ctx.send(gen_pass(count_password))

@bot.command()
async def coin(ctx):
     await ctx.send(flip_coin())

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def meme(ctx):
    with open('images/' + random.choice(os.listdir('images')), 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def capres(ctx):
    with open('images1/' + random.choice(os.listdir('images1')), 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def polusi(ctx):
    await ctx.send(f'Pencemaran atau polusi adalah masuk atau dimasukkannya mahluk hidup, zat, energi dan/ atau komponen lain ke dalam air atau udara. Pencemaran juga bisa berarti berubahnya tatanan (komposisi) air atau udara oleh kegiatan manusia dan proses alam, sehingga kualitas air/ udara menjadi kurang atau tidak dapat berfungsi lagi sesuai dengan peruntukkannya. Pencemaran terhadap lingkungan dapat terjadi di mana saja dengan laju yang sangat cepat, dan beban pencemaran yang semakin berat akibat limbah industri dari berbagai bahan kimia termasuk logam berat.')

@bot.command()
async def dampak_polusi(ctx):
    await ctx.send(f'menganggu keseimbangan lingkungan , punah nya flora fauna , kesuburan tanah berkurang , dll')

@bot.command()
async def cara_menangani_polusi(ctx):
    await ctx.send('''Kurangi menggunakan kendaraan bermotor. 
Matikan mesin mobil. 
Jangan membakar sampah. 
Menanam dan merawat pohon. 
Kurangi penggunaan energi di rumah.''')

@bot.command()
async def cara_membuat_kerajinan_plastik(ctx):
    await ctx.send('''Cara membuatnya: 
1. Potong sepertiga bagian bawah botol. 
2. Pada salah satu sisi, potong botol menjadi dua bentuk segitiga sehingga terlihat seperti telinga. 
3. Cat botol dengan warna yang diinginkan. 
4. Gambar wajah hewan pada botol, misalnya wajah kucing atau anjing. 
5. Isi botol dengan tanah dan tanaman yang ingin ditanam.''')


bot.run('token')
