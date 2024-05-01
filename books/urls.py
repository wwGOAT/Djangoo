from django.contrib import admin
from django.urls import path

from books.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', home_view)
]