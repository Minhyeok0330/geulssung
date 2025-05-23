"""
URL configuration for 글썽글썽 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from post import views

urlpatterns = [
    path("geulssung/", views.home_view, name="home"),  # /geulssung/
    path("geulssung/test/", views.test_page_view, name="test"), #/geulssung/test/
    path('admin/', admin.site.urls),
    path("geulssung/write/", views.write_post_view, name="write"),  # /geulssung/write
    path("geulssung/post/<int:post_id>", views.post_detail_view, name="post_detail"),  # /geulssung/post/1
    path("geulssung/accounts/", include("accounts.urls")), # /geulssung/accounts/
    path("geulssung/post/<str:nickname>/", views.public_posts_by_user, name="public_user_posts"),  # /geulssung/post/nickname
]
