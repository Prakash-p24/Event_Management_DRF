from .serializers import ItemSerializerOrg,ItemSerializerEve,ItemSerializerBook,ItemSerializerUser
from rest_framework.response import Response
from rest_framework import status
from .models import Organizer,Event,User,Bookings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime,date
import datetime


#list the organizers




#create the event



def Create(request):
    try:        # Get date from request
        event_date_str = request.data.get('date')
        if not event_date_str:
            return Response({"error": "Date is required"}, status=status.HTTP_400_BAD_REQUEST)
        datetime_object = datetime.datetime.strptime(event_date_str, '%Y-%m-%d')
        date_only_object = datetime_object.date()
        today = date.today()
        if date_only_object < today:
            return Response({"error": "Event cannot be created in the past"}, status=status.HTTP_400_BAD_REQUEST)

        event_title = request.data.get('title')
        if not event_title:
            return Response({"error": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)

        if Event.objects.filter(title=event_title).exists():
            return Response({"error": "This event already exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ItemSerializerEve(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status_code": status.HTTP_201_CREATED,
                "message": "Event Created Successfully",
                "Properties": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"error": f"Unable to create event: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)




    

#list the event
def EventList(request):
    try:
        events = Event.objects.all()
        if events:
            serializer = ItemSerializerEve(events, many=True)
            response_data = {
            "status_code": status.HTTP_200_OK,
            "Properties": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    except:
        return Response({"error": "Unable to Return Event"}, status=status.HTTP_400_BAD_REQUEST)


#create the user
def CreateUser(request):
    try:
        item = ItemSerializerUser(data=request.data)
        if User.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This User already exists')

        if item.is_valid():
            item.save()
            response_data = {
            "status_code": status.HTTP_201_CREATED,
            "message":"User Created Successfully",
            "Properties": item.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    except:
        return Response({"error": "Unable to Create User"}, status=status.HTTP_400_BAD_REQUEST)
    

#User list

def UserList(request):
    try:
        users = User.objects.all()
        if users:
            serializer = ItemSerializerUser(users, many=True)
            response_data = {
            "status_code": status.HTTP_200_OK,
            "Properties": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    except:
        return Response({"error": "Unable to Return User"}, status=status.HTTP_400_BAD_REQUEST)

#Booking
def CreateBookings(request):  
    try:
        event_ids = request.data.get('event_id')
        user_ids = request.data.get('user_id')
        queryset = Event.objects.get(event_id = event_ids)
    except:
        return Response({"Message":"Please enter valid Event","status_code":status.HTTP_400_BAD_REQUEST}) 

    try:
        booked = Bookings.objects.filter(event_id=event_ids,user_id=user_ids).exists()
        if booked:
            return Response({"Message":"You Already Booked this Event"})
    except:
        return Response({"Message":"Error occured in Filtering"})
    
    

    today = date.today()
    if queryset.date<today:
           return Response({"Message":"Event is Expired"})
    
    elif queryset.available_seats == 0:
           return Response({"Message":"Event is Fulled"})
        
    elif queryset:
        queryset.available_seats -=1
        queryset.save()
    item = ItemSerializerBook(data=request.data)
    try:
        if item.is_valid():
            item.save()
            response_data = {
            "status_code": status.HTTP_201_CREATED,
            "message":"Event Booked Successfully",
            "Properties": item.data
            }
        return Response(response_data, status=status.HTTP_201_CREATED)
    except:
        return Response({"Message":"Data is Invalid","status_code":status.HTTP_400_BAD_REQUEST})


#Partial Update User

def UpdateUser(request,pk):
    try:
        #payload
        # user_ids = request.data.get('user_id')
        # if not user_ids:
        #     return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        user_instance = User.objects.get(user_id=pk)
        serializer = ItemSerializerUser(user_instance, data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "status_code": status.HTTP_201_CREATED,
                "message":"User Updated Successfully",
                "Properties": serializer.data
                }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except:
        return Response({"error": "Unable to Update User"}, status=status.HTTP_400_BAD_REQUEST)
    
#Full Update User

def FullUpdateUser(request,pk):
    try:
        #payload
        # user_ids = request.data.get('user_id')
        # if not user_ids:
        #     return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        user_instance = User.objects.get(user_id=pk)
        serializer = ItemSerializerUser(user_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "status_code": status.HTTP_201_CREATED,
                "message":"User Updated Successfully",
                "Properties": serializer.data
                }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except:
        return Response({"error": "Unable to Update User"}, status=status.HTTP_400_BAD_REQUEST)
    
def DeleteUser(request):
    try:
        user_ids = request.data.get('user_id')
        if not user_ids:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        user_instance = User.objects.get(user_id=user_ids)
        
        # serializer = ItemSerializerUser(user_instance, data=request.data)
        if user_instance:
            user_instance.delete()
            response_data = {
                "status_code": status.HTTP_200_OK,
                "message":"User Deleted Successfully"
                }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
           return Response(status=status.HTTP_400_BAD_REQUEST)
        
    except:
        return Response({"error": "Unable to Update User"}, status=status.HTTP_400_BAD_REQUEST)
   

def CreateJWT(request):
    username = request.data.get("user_name")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(user_name=username)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    # Direct plain-text password check
    if user.password != password:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    # Generate JWT tokens
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    return Response({
        "user_id": str(user.id),
        "user_name": user.user_name,
        "access": access_token,
        "refresh": refresh_token
    }, status=status.HTTP_200_OK)
