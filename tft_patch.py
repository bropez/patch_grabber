from bs4 import BeautifulSoup as bs
import requests

import discord


patch_url_template = (
    "https://na.leagueoflegends.com/en/news/game-updates/patch/teamfight-tactics-patch-||||-notes"
)
patch_list_url = (
    "https://www.esportstales.com/teamfight-tactics/patch-notes-list"
)


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


def get_img_url(patch_url: str):
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
    # TODO: check which game to work with and clean that patch list
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
    # TODO: pass in the table_class to work with other games
    page = requests.get(patch_list_url)
    table_class = "sqs-block markdown-block sqs-block-markdown"

    soup = bs(page.text, 'html.parser')
    table = soup.findAll("div", {"class": table_class})[0]
    cleaned = clean_patches(table)

    return cleaned


def tft_rp():
    patch_num = get_all_patches()[0]
    patch_url = get_patch_url(patch_num)
    image_url = get_img_url(patch_url)
    
    response = get_response(patch_num, patch_url)

    ret_str = image_url + "||||" + response

    return ret_str


def tft_gp(patch_num: str):
    patch_url = get_patch_url(patch_num)
    image_url = get_img_url(patch_url)

    response = get_response(patch_num, patch_url)

    ret_str = image_url + "||||" + response

    return ret_str
