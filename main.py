import discord
import os
import requests
from keep_alive import keep_alive

client = discord.Client()

def helper():
  url = 'http://icanhazdadjoke.com/'
  headers = {'Accept': 'text/plain'}
  res = requests.get(url, headers=headers)
  return res.text
  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!joke'):
  
    await message.channel.send(helper())

keep_alive()
client.run(os.environ['TOKEN'])