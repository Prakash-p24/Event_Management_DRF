from .serializers import ItemSerializerOrg,ItemSerializerEve,ItemSerializerBook,ItemSerializerUser
from rest_framework.response import Response
from rest_framework import status
from .models import Organizer,Event,User,Bookings
from rest_framework import serializers

#list the organizers
def Org(request):
    try:
        organizer = Organizer.objects.all()
        if organizer:
            serializer = ItemSerializerOrg(organizer, many=True)
            response_data = {
            "status_code": status.HTTP_200_OK,
            "Properties": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    except:
        return Response({"error": "Unable to get Organizers"}, status=status.HTTP_400_BAD_REQUEST)



#create the event
def Create(request):
    try:
        event_title = request.data.get('title')
        print(event_title)
        item = ItemSerializerEve(data=request.data)
        if item.is_valid():
            print("one")
            if Event.objects.filter(title=event_title).exists():
               print("two")
               return Response({"error": "This data already exists"})
            else:
                print("three")
                item.save()
                response_data = {
                "status_code": status.HTTP_201_CREATED,
                "message":"Event Created Successfully",
                "Properties": item.data
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    except:
        return Response({"error": "Unable to Create Event"}, status=status.HTTP_400_BAD_REQUEST)
    

#list the event
def EventList(request):
    try:
        created = request.data.get('created_at')
        updated = request.data.get('updated_at')
        active = request.data.get('is_active')
        events = Event.objects.exclude(created_at = created,updated_at = updated,is_active = active)
        if events:
            serializer = ItemSerializerEve(events, many=True)
            response_data = {
            "status_code": status.HTTP_200_OK,
            "Properties": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
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
            return Response(status=status.HTTP_404_NOT_FOUND)
    
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
            return Response(status=status.HTTP_404_NOT_FOUND)
        
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
    
    if queryset:
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