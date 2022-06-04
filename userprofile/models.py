from statistics import mode
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

USER_STATUS_CHOICES = (
    ('active', 'active'),
    ('not-active', 'not-active'),
    ('suspicious', 'suspicious'),
    ('fraud', 'fraud'),
)

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', ' Others')
)

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(
        max_length=14,
        default='first_name'
    )
    last_name = models.CharField(
        max_length=14,
        blank=True, null=True
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    email = models.EmailField(
        max_length=30,
        blank=True, null=True
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True
    )
    referral_code = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        help_text='Don;t touch this field.This will fill automatically'
    )
    user_status = models.CharField(
        max_length=16,
        choices=USER_STATUS_CHOICES,
        default='active'
    )

    class Meta:
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.first_name


def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
