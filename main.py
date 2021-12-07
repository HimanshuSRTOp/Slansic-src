import discord
from discord.ext import commands

bot = commands.AutoShardedBot(command_prefix="~")

@bot.event
async def on_ready():
  print("Hello world")
  
bot.run("OTE3NjkzNzA0OTc2ODc1NTUw.Ya8a3Q.UZ7wgO6vMyOdsGQe_MGvae0SMao")
