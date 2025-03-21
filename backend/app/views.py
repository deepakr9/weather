from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    city = request.GET.get("city", "bengaluru")
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=17f2fbab506af2f13c75081cfec86b41&units=metric"
    api = requests.get(api_url).json()
    temp = api['main']['temp']
    country = api["sys"]["country"]
    city_name = api["name"]

    return render(request, "index.html", {"temp":temp, "country":country, "city":city_name})