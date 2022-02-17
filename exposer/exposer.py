from discord.ext import commands
import os

bot = commands.Bot()
TOKEN = os.environ['TOKEN']


@bot.event
async def on_ready():
  members = bot.guilds
  print(members)

  


bot.run(TOKEN)