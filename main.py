import discord # using discord api
from discord.ext import commands # for text commands

import nacl # for connecting to voice channels

TOKEN = 'MTA3NjU4NDAxMzU2MjY1MDY3NA.GuQDku.rK3aEH5AXBeHXV7-s43yIJ3Q0pgM62kxq70vys'

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

client = commands.Bot(command_prefix='!', intents=intents)

guildID= 1076579739466223786
voiceID = 1076579740296683644
textID = 1076579740296683643

@client.event
async def on_ready():
     print(f'{client.user} has joined the server.')
     generalText = client.get_channel(textID)
     await generalText.send('bot is here')


@client.command(name='join')
async def join(ctx):
    generalVoice = ctx.author.voice.channel
    await generalVoice.connect()


@client.command(name='disconnect')
async def disconnect(ctx):
    voiceClient = ctx.author.guild.voice_client
    await voiceClient.disconnect()


@client.command(name='play')
async def play(ctx, *arg):
    voiceClient = ctx.author.guild.voice_client
    if voiceClient.is_paused():
        voiceClient.resume()
    song_name = " ".join(arg)
    voiceClient.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg-5.1.2-essentials_build/bin/ffmpeg.exe", source='/Users/Mark/Music/' + song_name + '.mp3'))

@client.command(name='pause')
async def pause(ctx):
    voiceClient = ctx.author.guild.voice_client
    if voiceClient.is_paused == True:
        generalText = client.get_channel(textID)
        await generalText.send('No song to pause.')
    else:
        await voiceClient.pause()


@client.command(name='resume')
async def resume(ctx):
    voiceClient = ctx.author.guild.voice_client
    if voiceClient.is_paused:
        await voiceClient.resume()
    else:
        generalText = client.get_channel(textID)
        await generalText.send('No song to resume.')

@client.command(name='stop')
async def stop(ctx):
    voiceClient = ctx.author.guild.voice_client
    if voiceClient.is_playing:
        voiceClient.stop()
    else:
        generalText = client.get_channel(textID)
        await generalText.send('No song to stop.')

client.run(TOKEN)
