from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .services import Org,Create,EventList,CreateUser,UserList,CreateBookings,UpdateUser,FullUpdateUser,DeleteUser,CreateJWT
from rest_framework.response import Response

@api_view(['GET'])
def DisplayEvent(request):
    return EventList(request)

@api_view(['GET'])
def Hello(request):
    return Org(request)

@api_view(['POST'])
def CreateEvent(request):
    return Create(request)

@api_view(['POST'])
def CreateUsers(request):
    return CreateUser(request)

@api_view(['GET'])
def UsersList(request):
    return UserList(request)

@api_view(['POST'])
def Book(request):
    return CreateBookings(request)

@api_view(['PATCH'])
def UpdateUsers(request,pk):
    return UpdateUser(request,pk)

@api_view(['PUT'])
def FullUpdateUsers(request,pk):
    return FullUpdateUser(request,pk)

@api_view(['DELETE'])
def DeleteUsers(request):
    return DeleteUser(request)

@api_view(['POST'])
def CreateJwts(request):
    return CreateJWT(request)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Bookings

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_view(request):
    user = request.user
    print(user)

    # Get all bookings for this user
    user_bookings = Bookings.objects.filter(user_id=user, is_active=True).select_related('event_id')

    # Prepare booking + event details
    bookings_list = []
    for booking in user_bookings:
        event = booking.event_id
        bookings_list.append({
            "booking_id": str(booking.booking_id),
            "event_id": str(event.event_id),
            "title": event.title,
            "date": event.date,
            "time": event.time,
            "place": event.place,
            "event_type": event.event_type,
            "available_seats": event.available_seats,
            "total_seats": event.total_seats,
            "organizer_id": str(event.organizer_id.id),
            "booking_created_at": booking.created_at,
        })

    return Response({
        "user_id": str(user.id),
        "user_name": user.user_name,
        "bookings": bookings_list
    })


