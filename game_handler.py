from tft_patch import tft_rp, tft_gp

import discord


def get_embed(img_url: str):
    """Gets the discord.Embed object and sets an image to it

    Args:
        img_url (str): The url that the image is hosted at

    Returns:
        embed (discord.Embed): The discord.embed() object that has the image
    """
    embed = discord.Embed()
    embed.set_image(url=img_url)

    return embed


def clean_game(game_name: str):
    """Changes the game_name to lower case

    Args:
        game_name (str): The game name that needs to be lower cased

    Returns:
        game_name.lower() (str): The lower cased game name
    """
    return game_name.lower()


def get_patch_controller(game_name: str, patch_num: str):
    """The controller for getting a certain patch 

    Args:
        game_name (str): The specific game that you'd like to get a specific patch for
        patch_num (str): The patch number you'd like to get for the given game

    Returns:
        ret_str (str): The formatted string to be outputted to the discord server
    """
    switcher = {
        "tft": tft_gp,
    }

    clean_name = clean_game(game_name)
    bad_image = "https://cdn.pixabay.com/photo/2018/01/16/10/36/mistake-3085712_960_720.jpg"
    game_list = ", ".join(switcher.keys())
    bad_message = "We haven't implemented that game yet. Must be in the list of: {}".format(game_list)
    func = switcher.get(clean_name, lambda: "{}<splitter>{}".format(bad_image, bad_message))
    ret_str = func(patch_num)

    return ret_str


def recent_patch_controller(game_name: str):
    """The controller for getting the recent patch of a given game

    Args:
        game_name (str): The specific game that you'd like to get the recent patch for

    Returns:
        ret_str (str): The formatted string to be outputted to the discord server
    """
    # A switch statement for each game
    switcher = {
        "tft": tft_rp,
    }

    clean_name = clean_game(game_name)
    bad_image = "https://cdn.pixabay.com/photo/2018/01/16/10/36/mistake-3085712_960_720.jpg"
    game_list = ", ".join(switcher.keys())
    bad_message = "We haven't implemented that game yet. Must be in the list of: {}".format(game_list)
    func = switcher.get(clean_name, lambda: "{}<splitter>{}".format(bad_image, bad_message))
    ret_str = func()

    return ret_str

if __name__ == '__main__':
    words = recent_patch_controller('tft')
    one, two = words.split("<splitter>")
    print(one)
    print(two)
