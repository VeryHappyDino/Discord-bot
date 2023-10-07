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

# Inserisci il tuo token del bot Discord qui
TOKEN = 'MTE1NzYxODk4NTc5NDI4NTYxOA.Gsjw1T.JqaBVPiPOuAMvvTvM446kLDL2-Z5x3SAj9KmyQ'

client.run(TOKEN)