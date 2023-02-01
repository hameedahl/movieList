from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth # gets users from db
from .models import Profile
from .models import PopularMovie
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.

@login_required(login_url='login') # can not access feed page until you are logged in
def index(request):
        user_profile = Profile.objects.get(user=request.user)
        popularMovies = PopularMovie.objects.all()
        print(popularMovies)
        return render(request, 'index.html', {'user_profile': user_profile, "popular_movies" : popularMovies})

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
                                user_login = auth.authenticate(username=username, password=password)
                                auth.login(request, user_login)

                                # profile obj for new user
                                user_model = User.objects.get(username=username)
                                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                                new_profile.save()
                                return redirect('settings')

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

@login_required(login_url='login') # can not access feed page until you are logged in
def settings(request):
        user_profile = Profile.objects.get(user=request.user)
        if request.method == 'POST':
                if request.FILES.get('image') == None: # if there is no img sent
                        image = user_profile.profile_img # resubmit the og img
                        bio = request.POST['bio']
                        location = request.POST['location']

                        user_profile.profile_img = image
                        user_profile.bio = bio
                        user_profile.location = location
                        user_profile.save()
                if request.FILES.get('image') != None:
                        image = request.FILES.get('image')
                        bio = request.POST['bio']
                        location = request.POST['location']

                        user_profile.profile_img = image
                        user_profile.bio = bio
                        user_profile.location = location
                        user_profile.save()
                
                return redirect('settings')

        return render(request, 'settings.html', {'user_profile': user_profile})

def popularMovies(request):
                
                # get movie info
                url = f"https://imdb-api.com/en/API/Title/k_1pvaf6m4/{id}/Trailer,Ratings"
                response = requests.get(url)
                movie_obj = response.json()

                # get streaming info
                url = "https://streaming-availability.p.rapidapi.com/get/basic"
                querystring = {"country":"us","imdb_id":"tt1375666","output_language":"en"}
                headers = {
                        "X-RapidAPI-Key": "59acf3546cmsh0d1a19afef20499p135371jsn25d6436b4ae9",
                        "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)

                print(response.text['imdbID'])

        # url = "https://imdb-api.com/en/API/MostPopularMovies/k_1pvaf6m4"
        # response = requests.get(url)
        # # returns array of objects
        # movies = response.json()['items']

        # for movie in movies:
        #         id = movie['id']
        #         # get movie info
        #         url = f"https://imdb-api.com/en/API/Title/k_1pvaf6m4/{id}/Trailer,Ratings"
        #         response = requests.get(url)
        #         movie_obj = response.json()

        #         # get streaming info
        #         url = "https://streaming-availability.p.rapidapi.com/get/basic"
        #         querystring = {"country":"us","tmdb_id":id,"output_language":"en"}
        #         headers = {
        #                 "X-RapidAPI-Key": "59acf3546cmsh0d1a19afef20499p135371jsn25d6436b4ae9",
        #                 "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
        #         }
        #         response = requests.request("GET", url, headers=headers, params=querystring)

        #         print(response.text)
        #         movie_data = PopularMovie(
        #                 fullTitle = movie_obj['fullTitle'],
        #                 movie_id = movie_obj['id'],
        #                 image = movie_obj['image'],
        #                 releaseDate = movie_obj['releaseDate'],
        #                 runtimeStr = movie_obj['runtimeStr'],
        #                 plot = movie_obj['plot'],
        #                 stars = movie_obj['stars'],
        #                 genres = movie_obj['genres'],
        #                 countries = movie_obj['countries'],
        #                 languages = movie_obj['languages'],
        #                 contentRating = movie_obj['contentRating'],
        #                 ratings = movie_obj['ratings'],
        #                 trailer = movie_obj['trailer'],
        #                 keywords = movie_obj['keywords'],
        #                 similars = movie_obj['similars']
        #         )
        #         movie_data.save()
                return render(request, 'popularMovies.html')