# Create your views here.
from rest_framework.decorators import api_view
from .services import Org

@api_view(['GET'])
def Hello(request):
    return Org(request)