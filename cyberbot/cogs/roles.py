from discord.ext import commands
import asyncio


class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["roles", "getroles"], pass_context=True)
    async def get_roles(self, ctx):
        tmp = await ctx.send(*[x.name for x in ctx.author.roles[1:]])
        await asyncio.sleep(10)
        await tmp.delete()
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(roles(bot))
