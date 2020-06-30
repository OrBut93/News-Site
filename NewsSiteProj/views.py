from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoryForm, postForm
from .models import Post, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def is_valid_queryparam(param):
    return param != '' and param is not None


def home(request):
    posts = Post.objects.all().order_by('currentDate')
    categories = Category.objects.all()
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category_field')

    if is_valid_queryparam(date_min):
        posts = posts.filter(currentDate__gte=date_min)

    if is_valid_queryparam(date_max):
        posts = posts.filter(currentDate__lte=date_max)

    if is_valid_queryparam(category) and category != 'Choose...':
        posts = posts.filter(category__name=category)
        if category == 'All':
            posts = Post.objects.all().order_by('currentDate')

    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'NewsSiteProj/home.html', context)

    # posts = Post.objects.all().order_by('currentDate')
    # categories = Category.objects.all()
    # category = request.GET.get('category')
    # if category != "" and category is not None:
    #     posts.filter(category__name=category.name)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.viewsCounter = post.viewsCounter + 1
    post.save()
    return render(request, 'NewsSiteProj/detail.html', {'post': post})


def editpost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'GET':
        form = postForm(instance=post)
        return render(request, 'NewsSiteProj/editpost.html', {'post': post, 'form': form})
    else:
        try:
            form = postForm(request.POST, instance=post)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'NewsSiteProj/editpost.html', {'post': post, 'form': form, 'error': 'Bad Info'})


def removepost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'NewsSiteProj/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')


            except IntegrityError:
                return render(request, 'NewsSiteProj/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'That username has already been taken. Please choose a new username'})

        else:
            return render(request, 'NewsSiteProj/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'NewsSiteProj/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'NewsSiteProj/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            # username = request.POST['username']
            # # if username == 'admin':
            # #     return redirect('http://127.0.0.1:8000/admin')
            # # else:
            login(request, user)
            return redirect('home')


def createcategory(request):
    if request.method == 'GET':
        return render(request, 'NewsSiteProj/createcategory.html', {'form': CategoryForm()})
    else:
        form = CategoryForm(request.POST)
        newcategory = form.save(commit=False)
        newcategory.user = request.user
        newcategory.save()
        return redirect('home')


def createpost(request):
    if request.method == 'GET':
        return render(request, 'NewsSiteProj/createpost.html', {'form': postForm()})
    else:
        form = postForm(request.POST)
        newpost = form.save(commit=False)
        newpost.user = request.user
        newpost.save()
        return redirect('home')

# def category_list(request):
#     categories = Category.objects.all()
#     return render(request, 'blog/category_list.html', {
#         'categories': categories})  # blog/category_list.html should be the template that categories are listed.

# def filterCategories(request):
#     return render(Post.objects.all().get(Post.category.name == 'request'))
