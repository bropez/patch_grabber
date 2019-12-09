# TODO: grab picture from current patch link
#   maybe use <div class="field field-name-field-article-media field-type-file field-label-hidden"
#   as a starting point
from bs4 import BeautifulSoup as bs
import requests


def get_img_url(patch_url):
    # url = 'https://na.leagueoflegends.com/en/news/game-updates/patch/teamfight-tactics-patch-923-notes'
    page = requests.get(patch_url)
    div_class = "field field-name-field-article-media field-type-file field-label-hidden"
    a_class = "lightbox cboxElement"

    soup = bs(page.text, 'html.parser')
    thing = soup.findAll("div", {"class": div_class})
    thing2 = thing[0].findAll("a", {"class": a_class})
    thing3 = thing2[0].findAll("img", {"typeof": "foaf:Image"})
    img_url = "https://na.leagueoflegends.com{}".format(thing3[0]['src'])
    print(img_url)

    return img_url

# TODO: maybe use 'https://www.esportstales.com/teamfight-tactics/patch-notes-list'
#   to find out which patch is the current patch
