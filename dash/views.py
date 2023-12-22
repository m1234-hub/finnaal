from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm



@login_required(login_url='login.html')
def index(request):
      return render(request, 'index.html')


def pricing (request):
      return render(request, 'pricing.html')


def stockMarkets(request):
      return render(request, 'stock-markets.html')

def tradindViwe(request):
      return render(request, 'trading-view.html')


#@login_required(login_url='login.html')
def login_page( request):
      page = 'login'
      
      if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                  login(request, user)
                  
                  return redirect('index')

      return render(request, 'login.html', {'page': page})


def logoutUser(request):
      logout(request)
      return redirect('login')

def registerUser(request):
      page = 'register'
      form = CustomUserCreationForm()

      if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                  user = form.save(commit=False)
                  user.save()

                  user = authenticate(request, username=user.username, password=request.POST['password1'])

                  if user is not None:
                        login(request,user)
                        return redirect('index')


      context = {'form': form, 'page':page }
      return render(request, 'register.html', context)