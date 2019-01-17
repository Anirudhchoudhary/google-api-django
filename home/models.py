from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from oauth2client.contrib.django_util.models import CredentialsField
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)



class Event(models.Model):
    user = models.ForeignKey(User ,null=True ,blank=True, on_delete= models.CASCADE)
    name = models.CharField(max_length = 234,null = False , blank = 'false')
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    unique_id = models.CharField(null = True , blank = True , max_length = 232)


    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('home')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()