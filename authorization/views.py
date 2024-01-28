from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from authorization.forms import LoginForm, SignupForm


def index(request):
    return render(request, 'index.html')


def news(request):
    return render(request, 'news.html')


def like(request):
    return render(request, 'like.html')


def dislike(request):
    return render(request, 'dislike.html')


def for_dislike(request):
    return render(request, 'enter_duslike.html')


def news_for_hockey(request):
    return render(request, "news_for_hockey.html")


class Login(LoginView):
    redirect_authenticated_user = True
    # form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def user_comment(request):
    return render(request, 'comment.html')
