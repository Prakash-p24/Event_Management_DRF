from rest_framework.decorators import api_view
from .services import Org,Create,EventList,CreateUser,UserList,CreateBookings,UpdateUser,FullUpdateUser,DeleteUser

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

