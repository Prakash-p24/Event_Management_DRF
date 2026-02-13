from django.urls import path
from . import views


urlpatterns = [
    path('',views.Hello),
    path('create_event/',views.CreateEvent),
    path('event_list/',views.DisplayEvent),
    path('create_user/',views.CreateUsers),
    path('user_list/',views.UsersList),
    path('bookings/',views.Book),
    path('update_user/<uuid:pk>/',views.UpdateUsers),
    path('full_update/<uuid:pk>/',views.FullUpdateUsers),
    path('delete_user/',views.DeleteUsers),
    path('user_token/',views.CreateJwts),
    path('user_event/',views.subscribed_events),
]
