from discord.ext import commands
import data.settings as settings
import discord
import logging
import os


log = logging.getLogger("discord")
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))


class CyberBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=settings.PREFIX)

    async def on_ready(self):
        log.info(f"Logged in as {self.user.name}")
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                             name=f"yoolooo {len(self.guilds)}"))
        log.info("Changed presence")
        for cog in settings.cogs:
            self.load_extension(cog)


def run():
    client = CyberBot()
    client.run(settings.DISCORD_API_KEY)
