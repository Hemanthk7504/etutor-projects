from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from app.schemas.home import clothes_donation, verify_email, register,activation,login,dashboard

urlpatterns = [path("", clothes_donation, name="home"),
               path('register.html', register, name='register'),
               path('verify-email', verify_email, name='verify'),
               path('activate/<str:token>', activation, name='activate'),
               path('login.html', login, name='login'),
               path('dashboard',dashboard,name='dashboard')
               ]
urlpatterns += staticfiles_urlpatterns()

