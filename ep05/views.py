from django.shortcuts import render


def home(request):
    return render(request, "ep05/home.html", {})
