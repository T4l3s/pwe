from django.conf import settings

import requests as req
from bs4 import BeautifulSoup


def downloader(link):
    url = ""
