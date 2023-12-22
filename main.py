import asyncio
import os
import discord
from discord.ext import commands
from data.keys import token
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Yakışıklı güvenlik'))

    print(f'Discorda bağlandım. Hazırım şefim  {client.user}')


@client.tree.command(name="ping", description="Botun pingini gösterir.")
async def ping(interaction: discord.Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f"pingim: {bot_latency} ms")


# english_quiz_active = False
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load()
        await client.start(token)


asyncio.run(main())

# def get_random_word(learn_dict):
#    random_word = random.choice(list(learn_dict.keys()))
#    return random_word, learn_dict[random_word]
