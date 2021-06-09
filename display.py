import os
import webbrowser

import folium
import geopy


def get_coordinates(place):
    locator = geopy.Nominatim(user_agent="myGeocoder")
    location = locator.geocode(place)
    return [location.latitude, location.longitude]


def show(title):
    coordinates = get_coordinates(title)
    m = folium.Map()
    tooltip = title
    folium.Marker(
        get_coordinates(title), popup="<b>Timberline Lodge</b>", tooltip=tooltip
    ).add_to(m)
    filename = "index.html"
    m.save(filename)
    webbrowser.open('file://' + os.path.realpath(filename))


def show_array(titles):
    m = folium.Map()
    for title in titles:
        coordinates = get_coordinates(title)
        tooltip = title
        folium.Marker(
            get_coordinates(title), popup="<b>Timberline Lodge</b>", tooltip=tooltip
        ).add_to(m)
    filename = "index.html"
    m.save(filename)
    webbrowser.open('file://' + os.path.realpath(filename))
