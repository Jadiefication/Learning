import discord
import responses

intents = discord.Intents.default()
intents.message_content = True

async def send_message(message, user_message, is_private):
    try:
        responses = responses.handle_response(user_message)
        await message.author.send(responses) if is_private else await message.channel.send(responses)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    TOKEN = "MTE2NzgyNjU4MjYwMjI2NDY1Ng.GUdO7I.1WKohb8Ue-P0Tjrkru7u9B8RHXZeuL1la-jINY"
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f"{client.user} has connected to Discord!")
        
    client.run(TOKEN)
