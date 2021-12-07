import discord
from discord.ext import commands

bot = commands.AutoShardedBot(command_prefix="~")

@bot.event
async def on_ready():
  print("Hello world")
  
bot.run("TOKEN HERE")
