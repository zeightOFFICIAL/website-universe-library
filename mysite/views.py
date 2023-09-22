from django.shortcuts import render


def index_page(request):
    return render(request, "Index.html")


def about_page(request):
    return render(request, "About.html")
