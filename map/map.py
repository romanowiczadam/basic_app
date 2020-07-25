import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")

lat = [c for c in data['LAT']]
lon = [d for d in data['LON']]
elev = list(data['ELEV'])
name = list(data['NAME'])

def color_producer(x):
    if x > 3000:
        return 'red'
    elif x < 1500:
        return 'green'
    else:
        return 'orange'

map = folium.Map(location=[50.093582, 18.219791], zoom_start= 15, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanos")

for c_1, c_2, el, ne in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=[c_1, c_2], radius = 6, popup=str(el) + " m" + ne,
                               fill_color = color_producer(el), color = 'grey', fill=True,
                               fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
             style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                        else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map.html")
