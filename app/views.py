from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth # gets users from db
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login') # can not access feed page until you are logged in
def index(request):
        return render(request, 'index.html')

def signup(request):
        if request.method == 'POST':
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                password_confirm = request.POST['password_confirm']

                # form validation
                if password == password_confirm:
                        # check for dup emails
                        if User.objects.filter(email=email).exists():
                                messages.info(request, 'This email is taken')
                                return redirect('signup')
                        elif User.objects.filter(username=username).exists():
                                messages.info(request, 'This username is taken')
                                return redirect('signup')
                        else:
                                # no errors, so create user
                                user = User.objects.create_user(username=username, email=email, password=password)
                                user.save()
                                
                                # log user in set up profile

                                # profile obj for new user
                                user_model = User.objects.get(username=username)
                                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                                new_profile.save()
                                return redirect('login')

                else:
                        messages.info(request, 'Passwords do not match')
                        return redirect('signup')
        else:
                return render(request, 'signup.html')

def login(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                # check for user in db
                user = auth.authenticate(username=username, password=password)

                if user is not None:
                        auth.login(request, user)
                        return redirect('/')
                else:
                        messages.info(request, 'Incorrect username or password')
                        return redirect('login')
        else:
                return render(request, 'login.html')

@login_required(login_url='login') # only logout if you are logged in
def logout(request):
        auth.logout(request)
        return redirect('login')