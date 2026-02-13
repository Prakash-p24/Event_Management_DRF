from .serializers import ItemSerializerOrg
from rest_framework.response import Response
from rest_framework import status
from .models import Organizer
from rest_framework.response import Response
from rest_framework import status

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
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    except:
        return Response({"error": "Unable to get Organizers"}, status=status.HTTP_400_BAD_REQUEST)