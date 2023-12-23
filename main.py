import asyncio
import os
import random

import discord
from discord.ext import commands

from data.culture_data import cultures
from data.games import toss_up_list
from data.joke_data import jokes
from data.keys import token

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    await client.tree.sync()

    print(f'Discorda bağlandım. Hazırım şefim  {client.user}')


@client.tree.command(name="şaka", description="Şaka Yaparım.")
async def joke(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(jokes))


@client.tree.command(name="bilgi", description="Yeni Bir Bilgi Söylerim")
async def culture(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(cultures))


@client.tree.command(name="yazı-tura", description="Yazı Tura Oyunu")
async def tossUp(interaction: discord.Interaction):
    await interaction.response.send_message(f"Kazanan: {random.choice(toss_up_list)}")


@client.tree.command(name="ping", description="Botun pingini gösterir.")
async def ping(interaction: discord.Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f"pingim: {bot_latency} ms")


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load()
        await client.start(token)


asyncio.run(main())
