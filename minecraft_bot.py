import discord
from discord.ext import commands
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import minecraft_bot_commands as bot

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#BOT SETUP
intents: Intents = Intents.all() #Enables admin rights to the discord bot
Intents.message_content = True # A bit useless because this value is already set to true from the "Intents.all()"
client = commands.Bot(command_prefix='$', intents=intents) #Adding previously set rights and establishing "$" as a prefix for commands

#Retrieves informations of a server on MineHut's API
@client.command() #When a message starts with "$", considers it as a command to interprete
async def minecraft(ctx, request): #"ctx" stores values like the user and the channel while "request" store the text after the "$"
    r = bot.interprete_commands(request) #puts the text in the "interprete_commands" which verifies if the command is valid
    if(r != None): #If the "interprete" function returns something, normally a String, sends it as a message in the discord channel
        await ctx.send(r)


@client.event
async def on_ready()-> None:
    print(f'{client.user} is now running !') #Just a message to be sure the bot is up



client.run(TOKEN)