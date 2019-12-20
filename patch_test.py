# patch_test.py
import os

from discord.ext import commands
from dotenv import load_dotenv

from game_handler import recent_patch_controller, get_embed, get_patch_controller


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

# bot commands
@bot.command(name='get_patch', help="Gets the patch notes for the patch that is passed in.")
async def get_patch(ctx, game_name: str, patch_num: str):
    image_url, response = get_patch_controller(game_name, patch_num).split("<splitter>")
    embed = get_embed(image_url)

    await ctx.send(response, embed=embed)


@bot.command(name='recent_patch', help="Gets the most recent hard-coded patch for Team Fight Tactics.")
async def recent_patch(ctx, game_name: str):
    image_url, response = recent_patch_controller(game_name).split("<splitter>")
    embed = get_embed(image_url)

    await ctx.send(response, embed=embed)

bot.run(token)
