@bot.event
async def on_ready():
    print('Eingeloggt {}'.format(bot.user.name))
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        servers = list(bot.guilds) #Zählt die Bot Server
        await bot.change_presence(
            activity=discord.Activity(name='', type=discord.ActivityType.listening))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Activity(name='', type=discord.ActivityType.watching))
        await asyncio.sleep(30)
        await bot.change_presence(
            activity=discord.Activity(name='', type=discord.ActivityType.listening))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Activity(name='to {0} server'.format(str(len(servers))),    #Das, meine Damen und Herren
                                                            type=discord.ActivityType.watching))               #sagte dir, auf wie vielen Servern
        await asyncio.sleep(15) 
