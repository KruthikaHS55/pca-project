from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("slide1")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


@login_required
def slide1(request):
    return render(request, "slide1.html")

@login_required
def slide2(request):
    return render(request, "slide2.html")

@login_required
def slide3(request):
    return render(request, "slide3.html")

@login_required
def slide4(request):
    return render(request, "slide4.html")

@login_required
def slide5(request):
    return render(request, "slide5.html")

@login_required
def slide6(request):
    return render(request, "slide6.html")

@login_required
def slide7(request):
    return render(request, "slide7.html")

@login_required
def slide8(request):
    return render(request, "slide8.html")

@login_required
def slide9(request):
    return render(request, "slide9.html")

@login_required
def slide10(request):
    return render(request, "slide10.html")

