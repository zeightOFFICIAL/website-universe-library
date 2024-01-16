from django.shortcuts import render


def calculus_view(request):
    Head = '<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1"><link rel="icon" href="../static/Icons/LogoStrip.ico" charset="UTF-8"><title>Universe Library</title>'
    return render(request, "Calculus.html", {"head": Head})
