import discord

client = discord.Client()

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


print(discord.utils.oauth_url('793906134523969537'))
client.run('NzkzOTA2MTM0NTIzOTY5NTM3.X-zEtA.usA69HcQIhqUuutSmxisKklSGaM')
