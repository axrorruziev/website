"""
URL configuration for povtorenie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authorization.views import index, news_for_hockey, for_dislike, dislike,  like,  news,  Login, user_signup, user_logout, user_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('signup', user_signup, name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', user_logout, name='logout'),
    path('user_comment', user_comment, name='user_comment'),
    path('news', news, name='news'),
    path('like', like, name='like'),
    path('dislike', dislike, name='dislike'),
    path('dislike', for_dislike, name='for_dislike'),
    path('hockey', news_for_hockey, name='news_for_hockey')
]
