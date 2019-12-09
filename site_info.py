from bs4 import BeautifulSoup as bs
import requests

import discord


patch_url_template = (
    "https://na.leagueoflegends.com/en/news/game-updates/patch/teamfight-tactics-patch-||||-notes"
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
    thing = soup.findAll("div", {"class": div_class})
    thing2 = thing[0].findAll("a", {"class": a_class})
    thing3 = thing2[0].findAll("img", {"typeof": "foaf:Image"})
    img_url = "https://na.leagueoflegends.com{}".format(thing3[0]['src'])
    # print(img_url)

    return img_url


def get_embed(img_url: str):
    embed = discord.Embed()
    embed.set_image(url=img_url)

    return embed

# TODO: maybe use 'https://www.esportstales.com/teamfight-tactics/patch-notes-list'
#   to find out which patch is the current patch
def get_text(el):
    raw = el.text
    if ' - ' not in raw:
        return raw.strip()

    patch = raw.split(' - ')[1]
    patch_num = patch.split(' ')[1].strip()

    return patch_num



page = requests.get("https://www.esportstales.com/teamfight-tactics/patch-notes-list")
table_class = "sqs-block markdown-block sqs-block-markdown"

soup = bs(page.text, 'html.parser')
table = soup.findAll("div", {"class": table_class})
text_only = []
for div in table:
    text_only.append(get_text(div))

print(text_only)
