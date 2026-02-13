from rest_framework import serializers
from .models import Organizer

class ItemSerializerOrg(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        exclude = ['created_at','updated_at','is_active']