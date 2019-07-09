from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='bangalore')
'''
class UserProfile(models.Model):
    #username = models.ForeignKey(User,models.CASCADE)
    Keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    experince = models.IntegerField(default='0')
    phone = models.IntegerField(default='0')
    price = models.IntegerField(default='0')
    class Meta:
        db_table="UserProfile"

    bangalore = UserProfileManager()
    objects = models.Manager()

    def __str__(self):
        return self.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
'''
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import signals
from django.conf import settings
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    experince = models.CharField(max_length=5)
    phone = models.CharField(max_length=5)
    price = models.CharField(max_length=5)
    class Meta:
        db_table = "user_deatils"

'''
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
signals.post_save.connect(create_user_profile, sender=User)
'''
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
