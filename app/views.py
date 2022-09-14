import requests
from django.shortcuts import render
from django.urls import reverse

from app.models import Match


def dashboard(request):
    site = "http://127.0.0.1:8000/api/match/"
    response = requests.get(site).json()[0]
    data = {
        # "match": match,
        "response": response,
        "site": site,
            }
    return render(request, "dashboard.html", data)


def home(request):
    return render(request, "home.html")
