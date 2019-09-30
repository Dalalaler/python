from django.shortcuts import render
from pathlib import Path
from django.http import HttpResponse


def index(request):
    p = Path(__file__).parent / "index.html"
    with p.open("r") as f:
        return HttpResponse(f.read())

# Create your views here.
