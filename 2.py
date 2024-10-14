import discord
from discord.ext import commands

TOKEN = 'MTE0NDUxODM4MDAwMzUzMjg5Mg.GDNPsy.On8NCrSXH7DIv0ifXM6hHdlZDLmWvd_eVDN4gQ'

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def send_message(ctx, channel_id: int, *, message: str):
    """Mengirim pesan ke saluran berdasarkan ID saluran"""
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send(message)
        await ctx.send(f"Message sent to {channel.mention}: {message}")
    else:
        await ctx.send(f"Channel with ID {channel_id} not found.")


bot.run(TOKEN)
