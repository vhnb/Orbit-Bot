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
        color=discord.Colour(0x47b6b6)
    )
    
    await ctx.send(embed=embed)

@bot.command(name='ajuda')
async def help(ctx):
    ajuda = discord.Embed(
        description=(
            "# Comandos!\n"
            "``` .embed``` **Irá criar uma embed com o texto desejado.**\n"
            "```.criarc``` **Irá criar um canal de texto.**\n"
            "```.criarv``` **Irá criar um canal de voz.**\n"
            "```.apagar``` **Irá apagar a quantidade de mensagens desejada.**\n"
            "```.banir``` **Irá banir o membro específico.**\n"
            "```.expulsar``` **Irá expulsar o membro específico.**\n"
            "```.info``` **Irá puxar informações do membro desejado.**\n"
            "```.addcargo``` **Irá adicionar um cargo a um membro.**\n"
            "```.remcargo``` **Irá remover um cargo de um membro.**"
        ),
        color=discord.Colour(0x47b6b6)
    )

    await ctx.send(embed=ajuda)

@bot.command(name='apagar')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'{amount} mensagens foram apagadas por {ctx.author.mention}')

@bot.command(name='banir')
@commands.has_permissions(kick_members=True, ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} foi banido do servidor. **Razão:** {reason}')

@bot.command(name='expulsar')
@commands.has_permissions(kick_members=True, ban_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} foi expulso do servidor. **Razão:** {reason}')

@bot.command(name='info')
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

@bot.command(name='addcargo')
async def atribuir_cargo(ctx, membro: discord.Member, cargo_nome: str):
    if ctx.author.guild_permissions.administrator:
        cargo = discord.utils.get(ctx.guild.roles, name=cargo_nome)

        if cargo:
            await membro.add_roles(cargo)
            await ctx.send(f'O cargo {cargo_nome} foi atribuído a {membro.display_name}.')
        else:
            await ctx.send(f'O cargo {cargo_nome} não foi encontrado.')

    else:
        await ctx.send('Você não tem permissão para usar esse comando.')

@bot.command(name='remcargo')
async def remover_cargo(ctx, membro: discord.Member, cargo_nome: str):
    if ctx.author.guild_permissions.administrator:
        cargo = discord.utils.get(ctx.guild.roles, name=cargo_nome)

        if cargo:
            await membro.remove_roles(cargo)
            await ctx.send(f'O cargo {cargo_nome} foi removido de {membro.display_name}.')
        else:
            await ctx.send(f'O cargo {cargo_nome} não foi encontrado.')
    else:
        await ctx.send('Você não tem permissão para usar esse comando.')

@bot.command(name='ping')
async def ping(ctx):
    embed = discord.Embed(
        title='Pong! 🏓', 
        description=f'Ping = {round(bot.latency * 1000)} ms',
        color=discord.Colour(0x47b6b6)
        )
    embed.set_footer(text=f'Solicitado por {ctx.author}', icon_url=ctx.author.avatar.url)

    await ctx.reply(embed=embed)

@bot.event
async def on_ready():
    print(f'Bot esta on')

bot.run('token')

