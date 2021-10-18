import folium
import pandas
print('map1 EXECUTE!')

data=pandas.read_csv("Volcanoes.txt")

#print(data)
lat=list(data["LAT"])
lon=list(data["LON"])
elev = list(data["ELEV"])
name= list(data["NAME"])

def color_producer(elev):
    if elev<1000:
        return 'green'
    elif elev>3000:
        return 'blue'
    else:
        return 'red'


map=folium.Map(location=[38.58, -99.09], zoom_start=6,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes")

for lt,ln,el,nm in zip(lat,lon,elev,name):#goes on the two lists together.
    fgv.add_child(folium.Marker(location=[lt,ln], popup=nm + " " + str(el) + " m", icon=folium.Icon(color=color_producer(el))))#by default EL is float

fgp=folium.FeatureGroup(name="Population")

worldData=(open('world.json', 'r', encoding='utf-8-sig').read())#World BORDERS!
fgp.add_child(folium.GeoJson(worldData,
style_function=lambda x: {'fillColor':'white' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))#fill the color of the world to yellow

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
