import logging

import discord
from discord.ext import commands

from models.database import Session

from Cogs.Censor.obscene_words_filter import conf
from Cogs.Censor.obscene_words_filter.words_filter import ObsceneWordsFilter


session = Session()

logging.basicConfig(filename="censor.log", level=logging.INFO)

class Censor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        f = ObsceneWordsFilter(conf.bad_words_re, conf.good_words_re)
        returning = f.mask_bad_words(message.content)
        if returning != message.content:
            print(message.content)
            await message.channel.send(content=message.author.name + ":\n" + returning)
            await message.delete()


def setup(client):
    client.add_cog(Censor(client))