from bs4 import BeautifulSoup as bs
import requests

import discord


patch_list_url = "https://deadbydaylight.gamepedia.com/Patches"
# TODO: grab the link for each patch 
#   e.g. https://deadbydaylight.gamepedia.com/Patches#Patch_1.0.2a_-_30_June_2016

# List of functions in tft_patch.py
#   1. def get_patch_url(raw_patch_num: str):
#   2. def get_response(patch_num: str, patch_url: str):
#   3. def get_img_url(patch_url: str):
#   4. def clean_patches(table):
#   5. def get_all_patches():
#   6. def tft_rp():
#   7. def tft_gp(patch_num: str):