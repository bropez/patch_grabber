# patch_test.py
import os

from discord.ext import commands
from dotenv import load_dotenv

from site_info import (
    get_patch_url, get_response, 
    get_img_url, get_embed,
    get_all_patches
)


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

# bot commands
@bot.command(name='get_patch', help="Gets the patch notes for the patch that is passed in.")
async def get_patch(ctx, patch_num: str):
    patch_url = get_patch_url(patch_num)
    image_url = get_img_url(patch_url)

    embed = get_embed(image_url)

    response = get_response(patch_num, patch_url)
    await ctx.send(response, embed=embed)


@bot.command(name='recent_patch', help="Gets the most recent hard-coded patch for Team Fight Tactics.")
async def recent_patch(ctx):
    patch_num = get_all_patches()[0]
    patch_url = get_patch_url(patch_num)
    image_url = get_img_url(patch_url)

    embed = get_embed(image_url)
    
    response = get_response(patch_num, patch_url)
    await ctx.send(response, embed=embed)

bot.run(token)
