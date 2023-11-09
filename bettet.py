import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='?', intents=intents)
    
@bot.command(name='embed')
async def embed(ctx, *, content):
    clean_content = content.replace(f'{bot.user.mention}', '')
    embed = discord.Embed(
        description=clean_content,
        color=discord.Color.blue()
    )
    
    await ctx.send(embed=embed)

@bot.command(name='info')
async def send_message(ctx):
    user = ctx.message.author
    info = discord.Embed(
        title="**Como funciona?**",
        description="- Para criar uma embed, use o comando **'?embed'** e coloque o conteúdo da sua embed e marque o bot da Bettet.",
        color=discord.Color.blue()
    )

    await user.send(embed=info)

@bot.event
async def on_ready():
    print(f'Bot esta on')

bot.run('bot_token')

