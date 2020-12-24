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
    print("Kodluyoruz HACKATHON is ready to go!")
    kodluyoruzChannel = bot.get_channel(746850985510699092)


    for z in allNames:
        nameCounter = 0
        currentTeamMessage = "```\n"

        for j in z:
            print(j)

            currentTeamMessage += f"{}"
            currentTeamMessage += j
            currentTeamMessage += "\n"

        currentTeamMessage += "```"
        await kodluyoruzChannel.send(currentTeamMessage)


@bot.event
async def on_message(message):
    if (message.channel.id == 746850985510699092):
        for i in oneToTenEmojis:
            await message.add_reaction(i)
    else:
        pass


bot.run(token)
