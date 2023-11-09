import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.command(name='embed')
async def embed(ctx, *, content):
    embed = discord.Embed(
        description=content,
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f'Bot esta on')

bot.run('secrettoken!')

