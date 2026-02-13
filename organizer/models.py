from django.db import models
import uuid
# Create your models here.

class Organizer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) 
    phone_number = models.BigIntegerField()
    password = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default= True)


    class Meta:
        db_table = 'organizer'