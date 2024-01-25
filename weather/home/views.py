from django.shortcuts import render
import requests
import datetime
# Create your views here.

def home(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='Dehradun'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8f1f6a7f69fd19bd2bd26929f40b1278'
    PARAMS={'units':'metric'}
    data=requests.get(url,PARAMS).json()

    description=data['weather'][0]['description']
    icon= data['weather'][0]['icon']
    temp=data['main']['temp']

    day=datetime.date.today()


    return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'city':city,'day':day}) 

