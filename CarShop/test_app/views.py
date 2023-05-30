from datetime import date, timedelta

from django.db.models import Model
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Product, Bye, Provider

from .models import ProductType
import requests


def get_weather():
    appid = '91d45fb3f775b8f850579a41205a2a39'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'Minsk'
    res = requests.get(url.format(city)).json()

    return res["main"]["temp"]


def get_bitcoin():
    datetime_today = date.today()
    date_today = str(datetime_today)
    date_yesterday = str(datetime_today - timedelta(days=1))

    api = 'https://api.coindesk.com/v1/bpi/currentprice.json?start=' \
          + date_yesterday + '&end=' + date_today + '&index=[USD]'

    response = requests.get(api, timeout=2)  # get api response data from coindesk based on date range supplied by user
    response.raise_for_status()  # raise error if HTTP request returned an unsuccessful status code.
    prices = response.json()  # convert response to json format
    btc_price = prices.get("bpi")["USD"]["rate"]

    return btc_price


def index(request):

    sort = request.GET.getlist('sort')

    products = Product.objects.all().order_by(*sort)
    byes = Bye.objects.all()
    providers = Provider.objects.all()

    return render(request, "index.html", {
        "products": products,
        "providers": providers,
        "byes": byes,
        "temp": get_weather(),
        "bitc": get_bitcoin(),
    })






