from tft_patch import tft_rp, tft_gp

import discord


def get_embed(img_url: str):
    embed = discord.Embed()
    embed.set_image(url=img_url)

    return embed


def clean_game(game_name: str):
    return game_name.lower()


def get_patch_controller(game_name: str, patch_num: str):
    switcher = {
        "tft": tft_gp,
    }
    clean_name = clean_game(game_name)
    bad_image = "https://cdn.pixabay.com/photo/2018/01/16/10/36/mistake-3085712_960_720.jpg"
    game_list = ", ".join(switcher.keys())
    bad_message = "We haven't implemented that game yet. Must be in the list of: {}".format(game_list)
    func = switcher.get(clean_name, lambda: "{}||||{}".format(bad_image, bad_message))
    ret_str = func(patch_num)

    return ret_str


def recent_patch_controller(game_name: str):
    # TODO: make this a switch statement for each game

    # tft patch information
    switcher = {
        "tft": tft_rp,
    }

    clean_name = clean_game(game_name)
    bad_image = "https://cdn.pixabay.com/photo/2018/01/16/10/36/mistake-3085712_960_720.jpg"
    game_list = ", ".join(switcher.keys())
    bad_message = "We haven't implemented that game yet. Must be in the list of: {}".format(game_list)
    func = switcher.get(clean_name, lambda: "{}||||{}".format(bad_image, bad_message))
    ret_str = func()

    return ret_str

if __name__ == '__main__':
    words = recent_patch_controller('tft')
    one, two = words.split("||||")
    print(one)
    print(two)
