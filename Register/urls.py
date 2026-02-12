from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
    path('user_event/',views.protected_view),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
