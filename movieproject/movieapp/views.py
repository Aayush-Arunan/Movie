from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')



@login_required
def index(request):
    movie = Movie.objects.all()
    context = {'movie_list': movie}
    return render(request, "index.html", context)



@login_required
def detail(request, movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})


@login_required
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img = request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect("/")

    return render(request,'add.html')

@login_required
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(instance=movie)
    if(request.method=="POST"):
        form = MovieForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'edit.html',{'form':form})


@login_required
def delete(request,id):
        movie=Movie.objects.get(id=id)
        movie.delete()
        return index(request)

def Register(request):
    if(request.method=="POST"):
        U=request.POST['u']
        P=request.POST['p']
        CP=request.POST['cf']
        Fn=request.POST['fn']
        Ln=request.POST['ln']


        if(P==CP):
            user=User.objects.create_user(username=U,password=P,first_name=Fn,last_name=Ln)
            user.save()
            return index (request)
        else:
            return HttpResponse("Password are not same")
    return render(request,'Register.html')


def user_login(request):
    if(request.method=="POST"):
        U=request.POST['u']
        P=request.POST['p']
        user=authenticate(username=U,password=P)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse("Invalid Credentials")

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)


