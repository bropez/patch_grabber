# patch_test.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from site_info import get_img_url


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
patch_url_template = 'https://na.leagueoflegends.com/en/news/game-updates/patch/teamfight-tactics-patch-||||-notes'


def get_patch_url(raw_patch_num: str):
    patch_num = raw_patch_num.replace('.', '')
    patch_url = patch_url_template.replace('||||', patch_num)

    return patch_url


def get_response(patch_num: str, patch_url: str):
    response = (
        "Patch number: {}\n"
        "Check out the patch notes here: {}\n"
        .format(patch_num, patch_url)
    )

    return response


# bot commands
@bot.command(name='get_patch', help="Gets the patch notes for the patch that is passed in.")
async def get_specific_patch(ctx, patch_num: str):
    patch_url = get_patch_url(patch_num)
    image_url = get_img_url(patch_url)

    embed = discord.Embed()
    embed.set_image(url=image_url)

    response = get_response(patch_num, patch_url)
    await ctx.send(response, embed=embed)


@bot.command(name='recent_patch', help="Gets the most recent hard-coded patch for Team Fight Tactics.")
async def get_recent_patch(ctx):
    patch_num = "9.23"
    patch_url = get_patch_url(patch_num)
    image_url = get_img_url(patch_url)

    embed = discord.Embed()
    embed.set_image(url=image_url)
    
    response = get_response(patch_num, patch_url)
    await ctx.send(response, embed=embed)

bot.run(token)
