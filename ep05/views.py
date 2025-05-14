from django.shortcuts import render


def home(request):
    return render(request, "ep05/home.html", {})


def drf_examples(request):
    return render(request, "ep05/home.html", {})


def ninja_examples(request):
    return render(request, "ep05/home.html", {})
