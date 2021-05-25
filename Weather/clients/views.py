from django.shortcuts import render
from .models import Client, City
import requests
from .forms import CityForm
# Create your views here.

def indexView(request):
    #client = Client.objects.get(user=request.user)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=b2a2cb5e670e28ac458269e774226820'
    user = request.user 
    weather_data = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()    
    
    form = CityForm()        
    cities = City.objects.all()

    for city in cities:
        response = requests.get(url.format(city.name)).json()

        city_weather = {
            'name': city.name,
            'temp': int(response.get('main',{}).get('temp')),
            'main': response.get('weather',{})[0].get('main'),
            'temp_min': int(response.get('main',{}).get('temp_min')),
            'temp_max': int(response.get('main',{}).get('temp_max')),
            'icon': response['weather'][0]['icon'],
            'country': response['sys']['country']
        }        
        weather_data.append(city_weather) 
            
    context = {
        'user': user,
        'weather_data': weather_data,
        'form': form
        }   
    return render(request,'index.html',context)
    

