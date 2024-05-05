from django.urls import path
from .views import student_form, success

urlpatterns = [
    path('student/', student_form, name='student_form'),
    path('success/', success, name='success'),
]
