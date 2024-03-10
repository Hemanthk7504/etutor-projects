from django.urls import path,include

from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path("",index,name="index"),
    path("add_donor/",add_donor,name="add_donor"),
    path('add_bloodbank/', add_bloodbank, name='add_bloodbank'),
    path('donorlist/',donorlist,name="donorlist"),
    path('admin_login_view/',admin_login,name="admin_login"),
    path('delete_donor/<str:donor_email>/',delete_donor,name="delete_donor"),
    path('edit_donor/<str:donor_email>/', edit_donor, name="edit_donor"),
    path('donation_records/',donation_record,name="donation_record"),
    path('bloodbanklist/',bloodbanklist,name="bloodbanklist"),
    path('admin_login/',admin_login_view,name="admin_login_view"),
    path('register/',RegisterUser.as_view()),
    path('orm/', my_view, name='my_view'),
    path('statistics/',display_blood_donation_statistics,name="display_blood_donation_statistics"),
]
urlpatterns += staticfiles_urlpatterns()
