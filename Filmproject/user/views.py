from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Filmapp.models import Movie, Review
from .forms import MovieForm, ReviewForm, EditProfileForm


# Create your views here
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"Logged in Succefully.")
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name= request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST['email']
        password= request.POST['password']
        cpassword= request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                print("username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                print("email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect("register")
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        # Retrieve the movies added by the logged-in user
        user_movies = Movie.objects.filter(added_by=user)
        context = {'user': user, 'user_movies': user_movies}
        return render(request, 'profile.html', context)
    else:
        return redirect('login')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})



@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            # Set the added_by field to the current user before saving the movie
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect('/')  # Redirect to the movie list page after adding the movie
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})

def movie_reviews(request, genre_slug, movie_slug):
    movie = get_object_or_404(Movie, genre__slug=genre_slug, slug=movie_slug)
    reviews = Review.objects.filter(title=movie)
    return render(request, 'info.html', {'movie': movie, 'reviews': reviews})
@login_required
def add_review(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.title = movie
            review.user = request.user
            review.save()
            return redirect('Filmapp:filmInfo', genre_slug=movie.genre.slug, movie_slug=movie_slug)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'movie': movie})

def delete_movie(request, genre_slug, movie_slug):
    movie = get_object_or_404(Movie, genre__slug=genre_slug, slug=movie_slug)
    if request.method == 'POST':
        movie.delete()
        return redirect('user:profile')
    return render(request, 'confirm_delete.html', {'movie': movie})