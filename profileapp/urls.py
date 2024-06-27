# profiles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.profile_view, name='profile_view'),
    path('list/', views.add_project, name='add_project'),
]
