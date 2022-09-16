import discord
from discord.ext import commands
from setuptools import Command
from config import settings
import json
import requests
import urllib.request
import random

import googletrans
from googletrans import Translator

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
async def t(ctx, *, text):
    fraze = text
    translator = Translator()
    output = translator.translate(fraze)
    await ctx.send(output)
bot.run(settings['token'])    