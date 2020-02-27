#bot.py
import os
import random
import discord
import youtube_dl
from discord.ext import commands
from dotenv import load_dotenv

#dotenv in .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix = '.')

#when bot starts up it will tell us where it is connected in SHELL and all users connected
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n -'.join([member.name for member in guild.members])
    print(f'Guild Members:\n -{members}')

#on new user join event bot will send messgae to new member. 
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server! \n\n'
        "Don't be stinky."
    )

#command to create a new text channel
@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='new-channel', help = 'Use this command to create a new channel, admins only'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name = channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
    else: 
        await ctx.send('Channel with that name already exists')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command')


#command to give random brooklyn 99 quotes
@bot.command(name = '99', help = 'Responds with a random quote from Brooklyn 99')
# @commands.has_role(not ='CRAWMOMMY')
async def nine_nine(ctx):
    # if message.author == bot.user:
    #     return

    brooklyn_99_quotes = [
        "I'm the human form of the :100: emoji.",
        "Bingpot!",
        (
            "Cool. Cool cool cool cool cool cool cool, "
            "no doubt no doubt no doubt no doubt."
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name = 'roll', help = 'Simulates rolling dice, input # of dice and # of sides. In that order.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

import asyncio

player = {}

#supress noise about console usage from errors
youtube_dl.utils.bug_reports_mesage = lambda: ''

ytdl_format_options ={
    'format': 'bestaudio/best',
    # 'outtmpl': f'{extractor}s-{id}s-{title}s.{ext}s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcerticicate': True,
    'ignorerrors': False,
    'loglostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' #bind to ipv4 since ipv6 can cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

        @classmethod
        async def from_url(cls, url, *, loop=None, stream=False):
            loop = loop or asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

            if 'entries' in data:
                #take first item from a playlist
                data = data['entries'][0]

            filename = data ['url'] if stream else ytdl.prepare_filename(data)
            return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
    #joins a voice channel
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
        #plays a file form the local filesystem

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
        await print(f'Now playing: {query}')
        await ctx.send(f'Now playing {query}')

    @commands.command()
    async def yt(self, ctx, *, url):
        #plays from a url (almost anything youtube_dl suppports)
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}')if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def stream(self, ctx, *, url):
        #streams from a url (same as yt, but doesn't pre-download)
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after= lambda e: print(f'Player error: {e}'))

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def volume(self, ctx, volume:int):
        #changes player's volume
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"changed volume to {volume}.")

    @commands.command()
    async def stop(self, ctx):
    #stops and disconnects the bot from voice
        await ctx.voice_client.disconnect()

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self,ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connectd to a voice channel.")
                raise commands.CommandError("author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()




bot.add_cog(Music(bot))
bot.run(TOKEN)

