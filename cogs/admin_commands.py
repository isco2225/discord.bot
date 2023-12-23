from discord.ext import commands
import discord



class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.activities={}

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin Commands ready')

    @commands.command()
    async def change_status(self, ctx, activity, *, text):
        self.bind_text(text)
        await self.bot.change_presence(**self.activities.get(activity))

  #  @commands.command()
  #  async def change_status(self, ctx, activity, url, *, text):
  #      self.bind_text(text, url)
  #      await self.bot.change_presence(**self.activities.get(activity))

    def bind_text(self, text, url=''):
        self.activities = {
            "1": {'activity': discord.Game(name=text)},
            "2": {'activity': discord.Activity(type=discord.ActivityType.listening, name=text)},
            "3": {'activity': discord.Activity(type=discord.ActivityType.watching, name=text)},
            "4": {'activity': discord.Activity(name=text, url=url)}
        }



    @commands.command()
    async def clear(self, ctx, amount=2):
        if (ctx.author.name == "İSCO" and ctx.author.id == 450253516494209024) or (
                ctx.author.name == "aLMoRa" and ctx.author.id == 640602827168940082):
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.channel.send(f"Bu Yetkiye Sahip Değilsin..{ctx.author.mention}")


async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
