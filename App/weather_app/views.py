from django.shortcuts import render
import json
import urllib.request
# Create your views here.
URL = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q='
API_KEY = 'appid=5ba996966961cfac1d0c167bdddb0580'
def index(request):
	if request.method == 'POST':
		city = request.POST['search']
		res = urllib.request.urlopen(f"{URL}{city}&{API_KEY}").read()
		data = json.loads(res)
		weather_info = {
			'city' : str(data['name']),
			'city_code' : str(data['sys']['id']),
			'temp' : str(data['main']['temp']),
			'weather' : str(data['weather'][0]['main']),
		}
	else:
		weather_info = {}
	return render(request, 'index.html', {'data':weather_info})

