import math
import discord
import time
from emoji import EMOJI_ALIAS_UNICODE as EMOJIS
from discord.ext import commands
import sortNames

# Reading the token into "token"
f = open("token.0", "r")
token = f.read()
f.close()

# Declaring the official bot here
bot = commands.Bot(command_prefix="#")

# Declaring all the emojis to be reacted under the hackathon names messages
oneToTenEmojis = [EMOJIS[':one:'],
                  EMOJIS[':two:'],
                  EMOJIS[':three:'],
                  EMOJIS[':four:'],
                  EMOJIS[':five:'],
                  EMOJIS[':six:'],
                  EMOJIS[':seven:'],
                  EMOJIS[':eight:'],
                  EMOJIS[':nine:'],
                  EMOJIS[':ten:']]

# Creating a custom team names consisting message to be sent by the bot
allNames = sortNames.sort("teamNames.txt")


@bot.event
async def on_ready():
    global commonNumberCount

    kodluyoruzChannel = bot.get_channel(746850985510699092)

    for i in range(len(allNames)):
        nameCounter = 1
        currentTeamMessage = "```\n"
        commonNumberCount = len(allNames[i])
        
        for j in allNames[i]:
            print(j)

            currentTeamMessage += (f"{nameCounter} : " + j)
            currentTeamMessage += "\n"
            nameCounter += 1

        currentTeamMessage += "```"
        await kodluyoruzChannel.send(currentTeamMessage)


@bot.event
async def on_message(message):
    global commonNumberCount

    if (message.channel.id == 746850985510699092):
        for i in range(0, commonNumberCount):
            await message.add_reaction(oneToTenEmojis[i])
    else:
        pass


bot.run(token)
