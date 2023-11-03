from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

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

def film(request):
    return render(request, "film.html")

def meet(request):
    return render(request, "meet.html")

def login(request):
    if request.user.is_authenticated:
        return render(request, "user.html", {'name' : request.user.username })
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        is_valid = form.is_valid()
        print(is_valid)
        if is_valid:
            print(request.user.is_authenticated)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", { "form": form })

def logout_view(request):
    logout(request)
    return redirect('home')
