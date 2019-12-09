# patch_test.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from site_info import get_img_url


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='recent_patch', help='Gets the most recent hard-coded patch for Team Fight Tactics.')
async def get_patch(ctx):
    patch_num = "922"
    patch_url = 'https://na.leagueoflegends.com/en/news/game-updates/patch/teamfight-tactics-patch-{}-notes'.format(patch_num)
    image_url = get_img_url(patch_url)
    # image_link = 'https://na.leagueoflegends.com/sites/default/files/styles/scale_xlarge/public/upload/tft_patch_9.23_notes_header.jpg?itok=7hEN6D-X'

    embed = discord.Embed()
    embed.set_image(url=image_url)

    response = (
        "This is your current patch: {}\n"
        "Link to current patch notes: {}\n"
        .format(patch_num, patch_url)
    )
    await ctx.send(response, embed=embed)

bot.run(token)
