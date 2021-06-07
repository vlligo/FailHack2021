import os
import webbrowser

import folium
import wikipedia as wk
import requests
from bs4 import BeautifulSoup
import re
import numpy as np

wk.set_lang("en")


def get_coordinates(place):
    url = wk.page(place).url
    print(url)
    response = requests.get(url)
    if response:
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            lat_lon = soup.find("span", class_="geo-dec").text
            lat_lon_dd = [float(i) for i in re.findall("\\d+[.]\\d+", lat_lon)]
            if re.findall("\\w$", lat_lon)[0] == "S":
                lat_lon_dd[0] = -1 * lat_lon_dd[0]
            if re.findall("\\w$", lat_lon)[0] == "W":
                lat_lon_dd[1] = -1 * lat_lon_dd[1]
            lat, lon = lat_lon_dd
        except AttributeError:
            print("WARNING: No such location {}.".format(place))
            lat, lon = np.nan, np.nan
    else:
        print("WARNING: No such location {}.".format(place))
        lat, lon = np.nan, np.nan
    return [lat, lon]


def show(title):
    m = folium.Map(location=get_coordinates(title))
    filename = "index.html"
    m.save(filename)
    webbrowser.open('file://' + os.path.realpath(filename))
