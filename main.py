import os
import discord
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Connesso come {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/testa_o_croce'):
        risultato = random.choice(['Testa', 'Croce'])
        await message.channel.send(f'Hai lanciato una moneta e è uscito: {risultato}')

    if message.content.startswith('/numero_casuale'):
        risultato = random.choice(['Uno', 'Due', 'Tre', 'Quattro', 'Cinque'])
        await message.channel.send(f'Hai lanciato un numero casuale ed è uscito: {risultato}')
        
    if message.content.startswith("/meme"):
        
        names = os.listdir("images")
        random_image = names.random.choice(names)
        with open(f"./images/{random_image}","rb") as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
    if message.content.startswith("/memes animals"):
        names2 = os.listdir("memesanimals")
        random_animalmeme = names2.random.choice(names2)
        with open(f"./memesanimals/{random_animalmeme}","rb") as f:
            picture = discord.file(f)
        await message.channed.send(file=picture)
    if message.content.startswith("/memes_school"):
        names3 = os.listdir("memeschool")
        random_schoolmeme = names3.random.choice(names3)
        with open(f"./memeschool/{random_schoolmeme}","rb") as f:
            picture = discord.file(f)
        await message.channed.send(file=picture)
    if message.content.startswith("/weird_thought"):
        names4 = os.listdir("weird_thought")
        random_weirdthoughtmeme = names4.random.choice(names4)
        with open(f"./weird_thoughts/{random_weirdthoughtmeme}","rb") as f:
            picture = discord.file(f)
        await message.channed.send(file=picture)


# Inserisci il tuo token del bot Discord qui
TOKEN = 'MTE1NzYxODk4NTc5NDI4NTYxOA.GZyQa-.5mPb_8ifXOmkKTZtLfnqz5EH0HKYmFWY7Gy688'

client.run(TOKEN)
