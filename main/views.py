from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def terms(request):
    return render(request, "terms.html")

def shop(request):
    return render(request, "shop.html")