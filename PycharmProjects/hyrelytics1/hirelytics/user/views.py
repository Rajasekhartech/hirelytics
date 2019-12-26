from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import auth
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('user_home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
    return render(request,'profile.html')


def logout(request):
    auth.logout(request)
    return redirect('/')