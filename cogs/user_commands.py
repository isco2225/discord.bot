import random

from discord.ext import commands
import discord

from data.adjective_data import *


class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name="genel")
        await channel.send(f"Hoşgeldin {random.choice(good_adjecrives)},{member}")
        print(member)

    @commands.command()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name="genel")
        await channel.send(f"nereye gidiyon {random.choice(bad_adjecrives)}, {member}")
        print(member)

    @commands.command()
    async def selam(self, ctx):
        await ctx.send('as')


async def setup(bot):
    await bot.add_cog(UserCommands(bot))
