from django.shortcuts import render


def indexPage(request):
    return render(request, "index.html")


def aboutPage(request):
    return render(request, "about.html")
