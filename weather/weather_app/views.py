from django.shortcuts import render
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='Rajkot'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3460feb3e24b32456acb5dd45d97321c'
    PARAMS={'units':'metric'}
    data=requests.get(url,PARAMS).json()
    if data.get('cod') != 200:  # API returns cod 200 on success
        error = data.get('message', 'Error fetching weather')
        return render(request, 'index.html', {'error': error, 'city': city})

    description=data['weather'][0]['description']
    icon=data['weather'][0]['icon']
    temp=data['main']['temp']

    day=datetime.date.today()
    return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})
