from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
import uuid


class CustomUser(AbstractUser, PermissionsMixin):
    class Meta:
        permissions = [
            ('can_view_admin_page', 'Can view admin page'),
            ('can_view_user_page', 'Can view user page'),
        ]
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",
        blank=True,
    )

class Stoves(models.Model):
    INTERIOR = 'Int'
    EXTERIOR = 'Ext'
    LOCATION_CHOICES = [
        (INTERIOR, 'Interior'),
        (EXTERIOR, 'Exterior'),
    ]
    BEGINNER = 'Beginner'
    EXPERT = 'Expert'
    EXPERIENCE_CHOICES = [
        (BEGINNER, 'Beginner'),
        (EXPERT, 'Expert'),
    ]
    COLD = 'Cold'
    HOT = 'Hot'
    MIXED = 'Mixed'
    CLIMATE_CHOICES = [
        (COLD, 'Cold'),
        (HOT, 'Hot'),
        (MIXED, 'Mixed'),
    ]
    COOKING = 'Cooking'
    HEATING = 'Heating'
    OTHER = 'Other'
    USE_CHOICES = [
        (COOKING, 'Cooking'),
        (HEATING, 'Heating'),
        (OTHER, 'Other'),
    ]

    stove_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stove_url = models.URLField()
    dimensions = models.CharField(255)
    experience = models.CharField(max_length=8, choices=EXPERIENCE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    climate = models.CharField(max_length=5, choices=CLIMATE_CHOICES)
    stove_location =  models.CharField(max_length=3, choices=LOCATION_CHOICES)
    use = models.CharField(max_length=7, choices=USE_CHOICES)

class Materials(models.Model):
    material_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stove_id = models.ForeignKey(Stoves, on_delete=models.CASCADE)
    material_name = models.CharField(255)

class Reviews(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    RATING_CHOICES = [
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
    ]
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stove_id = models.ForeignKey(Stoves, on_delete=models.CASCADE)
    rating = models.CharField(max_length=2, choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class History(models.Model):
    history_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stove_id = models.ForeignKey(Stoves, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


