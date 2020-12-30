import discord
import os

client = discord.Client()
ROBOFRIEND_CLIENT_ID = os.environ["ROBOFRIEND_CLIENT_ID"]
ROBOFRIEND_DISCORD_TOKEN = os.environ["ROBOFRIEND_DISCORD_TOKEN"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send(f'Hello {message.author.name.split("#")[0]}!')

    if message.content.startswith('!roast'):
        await message.channel.send("Dang son!")


print(discord.utils.oauth_url(ROBOFRIEND_CLIENT_ID))
client.run(ROBOFRIEND_DISCORD_TOKEN)
