from django.db import models
import uuid

class Organizer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) 
    phone_number = models.BigIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default= True)


    class Meta:
        db_table = 'organizer'     


class Event(models.Model): 
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    available_seats = models.IntegerField()
    total_seats = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default= True)

    organizer_id = models.ForeignKey(
        Organizer,
        to_field='id',
        on_delete=models.CASCADE,
        db_column='organizer_id'
        
    )


    class Meta:
        db_table = 'event' 

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default= True)

    class Meta:
        db_table = 'user'



class Bookings(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(
        User,
        to_field='user_id',
        on_delete=models.CASCADE,
        db_column='user_id'
        
    )
    event_id = models.ForeignKey(
        Event,
        to_field='event_id',
        on_delete=models.CASCADE,
        db_column='event_id'
        
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default= True)

    class Meta:
        db_table = 'bookings'

