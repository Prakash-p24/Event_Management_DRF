from django.urls import path
from . import views
urlpatterns = [
    path('organizer_list/',views.Hello)
]