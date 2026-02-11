from django.urls import path
from . import views

urlpatterns = [
    path('',views.Hello),
    path('create_event/',views.CreateEvent),
    path('event_list/',views.DisplayEvent),
    path('create_user/',views.CreateUsers),
    path('user_list/',views.UsersList),
    path('bookings/',views.Book),
    path('update_user/',views.UpdateUsers),
    path('full_update/',views.FullUpdateUsers),
    path('delete_user/',views.DeleteUsers)
]
