from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount=2):
        if (ctx.author.name == "İSCO" and ctx.author.id == 450253516494209024) or (
                ctx.author.name == "aLMoRa" and ctx.author.id == 640602827168940082):
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.channel.send(f"Bu Yetkiye Sahip Değilsin..{ctx.author.mention}")


    @commands.command()
    async def naberrrs(self, ctx):
        await ctx.send('as')



def setup(bot):
    bot.add_cog(Events(bot))
