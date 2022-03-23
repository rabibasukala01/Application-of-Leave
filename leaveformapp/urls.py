from django.urls import path
from . import views


urlpatterns = [
    path('', views.form, name='form'),
    path('applicants-lists', views.listofapplicants, name='applicants')
]
