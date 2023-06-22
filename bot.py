import nextcord
from nextcord.ext import commands
import datetime
import random

# Configuración del bot
TOKEN = 'tu_token_de_discord'

#intents
intents = nextcord.Intents.default()
intents.message_content = True

# Agreguemos el prefix para el bot
bot = commands.Bot(command_prefix='!', intents=intents)

# ¿Qué dice el bot cuando está conectado? Pues...
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}') # Puedes modificarlo también.

# 1. Comando !hola
@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola!')

# 2. Comando !adios
@bot.command()
async def adios(ctx):
    await ctx.send('¡Adiós!')

# 3. Comando !hora
@bot.command()
async def hora(ctx):
    now = datetime.datetime.now()
    hora_actual = now.strftime("%H:%M:%S")
    await ctx.send(f'La hora actual es: {hora_actual}')

# 4. Comando !chiste
@bot.command()
async def chiste(ctx):
    chistes = [
        'Habia una vez un perro llamado Calcetín, llegó alguien y se lo puso.',
        'Proximamente mas chistes. ## 2 ##',
        'Proximamente mas chistes. ## 3 ##'
    ]
    chiste_random = random.choice(chistes)
    await ctx.send(chiste_random)

# Comando !dado
@bot.command()
async def dado(ctx):
    resultado = random.randint(1, 6)
    await ctx.send(f'El dado ha caído en el número {resultado}.')

# Comando !ayuda
@bot.command()
async def ayuda(ctx):
    embed = nextcord.Embed(title='Comandos disponibles', description='Aquí tienes una lista de comandos disponibles y lo que hacen:')
    embed.add_field(name='!hola', value='Saluda al bot.', inline=False)
    embed.add_field(name='!adios', value='Despide al bot.', inline=False)
    embed.add_field(name='!hora', value='Muestra la hora actual.', inline=False)
    embed.add_field(name='!chiste', value='Muestra un chiste gracioso.', inline=False)
    embed.add_field(name='!dado', value='Simula el lanzamiento de un dado.', inline=False)
    await ctx.send(embed=embed)

# Iniciemos el bot...
bot.run(TOKEN)