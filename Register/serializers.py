from rest_framework import serializers
from .models import Organizer,Event,User,Bookings

class ItemSerializerOrg(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        exclude = ['created_at','updated_at','is_active']

class ItemSerializerEve(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['created_at','updated_at','is_active']


class ItemSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['created_at','updated_at','is_active']


class ItemSerializerBook(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        exclude = ['created_at','updated_at','is_active']