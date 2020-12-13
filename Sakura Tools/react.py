import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='') # Dein Prefix
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Eingeloggt {}'.format(bot.user.name))
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        await bot.change_presence(
            activity=discord.Activity(name='', type=discord.ActivityType.listening))
        await asyncio.sleep(15)
        


@bot.event
async def on_ready():
    print (" ") #message
 
 
@bot.event
async def on_message(message):
    if(message.channel.id == " "): #channel_id
        await bot.add_reaction(message, "discord_emote_id_here") #emote_id




bot.run(' ')
