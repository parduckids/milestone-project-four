"""
URL configuration for subsurface project.

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
from django.urls import path, include

# all urls in the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('event.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('', include('contact.urls')),
    path('', include('tickets.urls')),
]
# add differrent error page urls for common errors
handler404 = 'subsurface.views.custom_404'
# handler500 = 'subsurface.views.custom_500'
handler403 = 'subsurface.views.custom_403'
handler400 = 'subsurface.views.custom_400'