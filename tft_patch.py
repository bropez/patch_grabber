from bs4 import BeautifulSoup as bs
import requests

import discord


patch_url_template = (
    "https://na.leagueoflegends.com/en/news/game-updates/patch/teamfight-tactics-patch-<patch_placeholder>-notes"
)
patch_list_url = (
    "https://www.esportstales.com/teamfight-tactics/patch-notes-list"
)


def get_patch_url(raw_patch_num: str):
    """Gets the url of the chosen patch's patch notes.
    Args:
        raw_patch_num (str): The patch number that you'd like to view

    Returns:
        patch_url (str): The str of the passed in patch's patch notes
    """
    patch_num = raw_patch_num.replace('.', '')
    patch_url = patch_url_template.replace('<patch_placeholder>', patch_num)

    return patch_url


def get_response(patch_num: str, patch_url: str):
    """Creates the response that the discord bot will say in the text chat.

    Args:
        patch_num (str): The wanted patch
        patch_url (str): The url of the specific patch's patch notes

    Returns:
        response (str): The formatted string that will be sent through a discord text channel
    """
    response = (
        "Patch number: {}\n"
        "Check out the patch notes here: {}\n"
        .format(patch_num, patch_url)
    )

    return response


def get_img_url(patch_url: str):
    """Gets the url of the banner image in the patch notes page.

    Args:
        patch_url (str): The url of the patch notes

    Returns:
        img_url (str): The url of the banner image
    """
    page = requests.get(patch_url)
    div_class = "field field-name-field-article-media field-type-file field-label-hidden"
    a_class = "lightbox cboxElement"

    soup = bs(page.text, 'html.parser')
    divs = soup.findAll("div", {"class": div_class})[0]
    links = divs.findAll("a", {"class": a_class})[0]
    imgs = links.findAll("img", {"typeof": "foaf:Image"})
    img_url = "https://na.leagueoflegends.com{}".format(imgs[0]['src'])

    return img_url
    
    
def clean_patches(table):
    """Trims the white space and dates from the patch list so only patch numbers remain.

    Args:
        table: The table from the web page to be iterated through

    Returns:
        patch_list (list): A list of all patch numbers
    """
    # TODO: check which game to work with and clean that patch list
    #   maybe lift this out of tft_patch.py and have it callable by other games
    patch_list = []

    for div in table:
        if ' - ' not in div.text:
            continue

        raw = div.text
        patch = raw.split(' - ')[1]
        patch_num = patch.split(' ')[1].strip()

        patch_list.append(patch_num)

    return patch_list


def get_all_patches():
    """Gets all of the patches for only Teamfight Tactics currently.

    Args:
        No Arguments

    Returns:
        cleaned (list): A list of all patch notes
    """
    # TODO: pass in the table_class to work with other games
    page = requests.get(patch_list_url)
    table_class = "sqs-block markdown-block sqs-block-markdown"

    soup = bs(page.text, 'html.parser')
    table = soup.findAll("div", {"class": table_class})[0]
    cleaned = clean_patches(table)

    return cleaned


def tft_rp():
    """Gets the recent patch for Teamfight Tactics.

    Args:
        No Arguments

    Returns:
        ret_str (str): The string that will be sent through the discord text channel
    """
    patch_num = get_all_patches()[0]
    patch_url = get_patch_url(patch_num)
    image_url = get_img_url(patch_url)
    
    response = get_response(patch_num, patch_url)

    ret_str = image_url + "<splitter>" + response

    return ret_str


def tft_gp(patch_num: str):
    """Gets the patch of the given patch number for Teamfight Tactics.

    Args:
        patch_num (str): The patch number that you'd like to view

    Returns:
        ret_str (str): The string that will be sent through the discord text channel
    """
    patch_url = get_patch_url(patch_num)
    image_url = get_img_url(patch_url)

    response = get_response(patch_num, patch_url)

    ret_str = image_url + "<splitter>" + response

    return ret_str
