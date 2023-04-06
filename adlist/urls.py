"""adlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin, auth
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),  # Keep
    path('ads/', include('ads.urls'))

]


try:
    from adlist.settings import SOCIAL_AUTH_GITHUB_KEY
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth.views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except Exception as e:
    print('Using registration/login.html as the login template')