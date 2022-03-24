from django.urls import path
from . import views


urlpatterns = [
    path('', views.form, name='form'),
    path('applicants-lists/', views.listofapplicants, name='applicants'),
    path('applicants-lists/1', views.first_year, name='firstyear'),
    path('applicants-lists/2', views.second_year, name='secondyear'),
    path('applicants-lists/3', views.third_year, name='thirdyear'),
    path('applicants-lists/4', views.fourth_year, name='fourthyear'),
]
