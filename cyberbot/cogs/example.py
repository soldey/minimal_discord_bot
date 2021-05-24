from discord.ext import commands


class example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def example(self, ctx):
        user_name = ctx.author.name
        await ctx.send(f"{user_name}, hello!")
        await ctx.send(user_name + ", hello!")
        await ctx.send("{0}, hello!".format(user_name))


def setup(bot):
    bot.add_cog(example(bot))
