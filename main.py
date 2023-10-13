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

# Inserisci il tuo token del bot Discord qui
TOKEN = 'MTE1NzYxODk4NTc5NDI4NTYxOA.G9Tow9._xdzxCG6TmSfLu_sDylmDlmBOuWzGKC4oShruA'

client.run(TOKEN)
