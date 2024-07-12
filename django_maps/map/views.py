from django.shortcuts import render
from .models import Location
import folium
from folium.plugins import FastMarkerCluster # Esta función me va a permitir hacer que se agrupen las sucursales si hago un zoom out

# Create your views here.
def home(request):
    # inicializo el mapa
    initialMap = folium.Map(location=[-31.412167, -64.186832], zoom_start=12)
    
    
    # Recupero todas las locaciones de las sucursales
    locations = Location.objects.all()

    # Creo dos listas, una para las latitudes y otra para las longitudes de las sucursales    
    latitudes = [location.lat for location in locations]
    longitudes = [location.lng for location in locations]

    # con zip hago tuplas de latitud-longitud de las sursales y con list las convierto en listas
    # con FastMarkerCluster creo los cluster y con add_to los agrego al mapa
    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(initialMap)
    
    # El siguiente código queda comentado ya que es reemplazado por el clustering, que también agrega los marcadores
    # Agrego los pines en el mapa de acuerdo a las coord de las sucursales
    # for location in locations:
    #     coordinates = (location.lat, location.lng)
    #     # Agrego el pin al mapa
    #     folium.Marker(coordinates, popup=location.name).add_to(initialMap)
        
    context = {'map': initialMap._repr_html_(),
               'locations': locations}
    return render (request, 'map/home.html', context)


