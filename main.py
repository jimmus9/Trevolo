#IMPORTS
import discord
from discord.ext import commands
from AntiScam import AntiScam
import os


#envs variables
TOKEN = os.environ['TOKEN']
USER1 = os.environ['USER1']
USER2 = os.environ['USER2']
LOGS = os.environ['LOGS']



#ANTI SPAM-SCAM
whitelist = [] 
logs_channel = 942249195048427561

bot = commands.Bot(command_prefix='>')
bot.remove_command('help') 

#MENSAJE DE LISTO
@bot.event
async def on_ready():
  print('Estoy listo, soy {0.user}'.format(bot))
  
  

#MUTEDHAMMER
@bot.listen()
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='Muted', verified_role='Ok', logs_channel=logs_channel) 

@bot.event
async def on_message(saludo):
    #para que no lea sus mensajes
    if saludo.author == bot.user:
        return
    if saludo.content.startswith('hola'):
        await saludo.channel.send('pa mi tu cola')

  
  

bot.run(TOKEN)