import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='.', intents=intents)
    
@bot.command(name='embed')
async def embed(ctx, *, content):
    clean_content = content.replace(f'{bot.user.mention}', '')
    embed = discord.Embed(
        description=clean_content,
        color=discord.Color.blue()
    )
    
    await ctx.send(embed=embed)

@bot.command(name='ajuda')
async def help(ctx):
    ajuda = discord.Embed(
        title="**Comandos Bettet!**",
        description=(
            "**- .criarc** Irá criar um canal de texto.\n"
            "**- .criarv** Irá criar um canal de voz.\n"
            "**- .apagar** Irá apagar a quantidade de mensagens desejada.\n"
            "**- .ban** Irá banir o membro específico.\n"
            "**- .expulsar** Irá expulsar o membro específico.\n"
            "**- .user** Irá puxar informações do membro desejado."
        ),
        color=discord.Color.blue()
    )

    await ctx.send(embed=ajuda)

@bot.command(name='apagar')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'{amount} mensagens foram apagadas por {ctx.author.mention}')

@bot.command(name='ban')
@commands.has_permissions(kick_members=True, ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} foi banido do servidor. **Razão:** {reason}')

@bot.command(name='expulsar')
@commands.has_permissions(kick_members=True, ban_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} foi expulso do servidor. **Razão:** {reason}')

@bot.command(name='user')
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f'**Nome:** {member.name}\n**Apelido:** {member.display_name}\n**ID:** {member.id}\n**Entrou no Servidor:** {member.joined_at}\n**Conta Criada:** {member.created_at}')

@bot.command(name='criarc')
@commands.has_permissions(manage_channels=True)
async def createch(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)

    if not existing_channel:
        new_channel = await guild.create_text_channel(channel_name)
        await ctx.send(f'Canal "{channel_name}" criado com sucesso!')
    else:
        await ctx.send(f'O canal "{channel_name}" já existe.')

@bot.command(name='criarv')
@commands.has_permissions(manage_channels=True)
async def create_voice_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.voice_channels, name=channel_name)

    if not existing_channel:
        new_channel = await guild.create_voice_channel(channel_name)
        await ctx.send(f'Canal de voz "{channel_name}" criado com sucesso!')
    else:
        await ctx.send(f'O canal de voz "{channel_name}" já existe.')

@bot.event
async def on_ready():
    print(f'Bot esta on')

bot.run('token')
