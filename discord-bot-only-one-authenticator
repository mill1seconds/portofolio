import discord, os

from discord.channel import DMChannel

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('Connected to discord as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.author.id == YOUR_DISCORD_ID: # Enter your Discord user ID
        
        if message.content.startswith('/YOUR_COMMAND1'):
            await message.channel.send('MESSAGE')
        
        if message.content.startswith('/YOUR_COMMAND2'):
            await message.channel.send('MESSAGE')

        if message.content.startswith('/YOUR_COMMAND3'):
            await message.channel.send('MESSAGE')

        if message.content.startswith('/YOUR_COMMAND4'):
            await message.channel.send('MESSAGE')

        if message.content.startswith('/YOUR_COMMAND5'):
            await message.channel.send('MESSAGE')

        if message.content.startswith('/YOUR_COMMAND6'):
            await message.channel.send('MESSAGE')

        if message.content.startswith('/YOUR_COMMAND7'):
            await message.channel.send('MESSAGE')

        if message.content.startswith('/YOUR_COMMAND8'):
            await message.channel.send('MESSAGE')

        if message.content.startswith('/YOUR_COMMAND9'):
            await message.channel.send('MESSAGE')

    # Add all your commands as you wish
        
    else:
        await message.channel.send(':warning: **You are not authorized to use this bot**')
    
try:
  client.run(os.getenv('TOKEN')) # You can enter your bot token in "SECRETS"
except Exception as err:
  raise err
