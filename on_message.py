import discord

client = discord.Client()

@client.event
async def on_ready():
    print("the bot is now online")

client.run("OTg4NTAxMTQ5NzIyMjQzMTU0.G33M1-.aQCqmjnmH7SwU8-Hq3a2ARVkUJNzd95wtZocQ0")