from keep_alive import keep_alive
import discord
import openai
import os


openai.api_key = os.environ.get("CHATGPT_API_KEY")

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        response = generate_response(message.content)
        await message.channel.send(response)
        
    # Check if the bot is mentioned in the message
    elif client.user in message.mentions:
        response = generate_response(message.content)
        await message.channel.send(response)

def generate_response(prompt):
    # Call OpenAI's API to generate a response based on the prompt
    response = openai.Image().create(
        prompt=prompt,
        n=1,
        size='1920x1080'
    )

    return response['data'][0]['url']


keep_alive()
client.run(os.environ.get("DISCORD_BOT_TOKEN"))