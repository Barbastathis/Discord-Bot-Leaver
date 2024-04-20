import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)
token = "YOUR_BOT_TOKEN"

# discord guild ids you don't want to leave
whitelist = [
    123456789012345678,
    696969696969696969
]


@client.event
async def on_ready():
    for guild in client.guilds:
        try:
            if guild.id not in whitelist:
                server = client.get_guild(guild.id)
                await server.leave()
                print(f"Left {server.name} ({server.id})")
        except Exception as e:
            print(e)
    print("Done")


client.run(token)