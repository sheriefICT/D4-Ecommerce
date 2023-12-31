from django.db import models

class company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company')
    suptitle = models.TextField(max_length=500)
    fasebook_link = models.URLField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(max_length=200, null=True, blank=True)
    youtube_link = models.URLField(max_length=200, null=True, blank=True)
    phones = models.TextField(max_length=20, null=True, blank=True)
    email = models.TextField(max_length=200, null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    android_app = models.URLField(max_length=200, null=True, blank=True)
    ios_app = models.URLField(max_length=200, null=True, blank=True)
    call_us = models.CharField(max_length=100)
    email_us = models.CharField(max_length=100)

    def __str__(self):
        return self.name