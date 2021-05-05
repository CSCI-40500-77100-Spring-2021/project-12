from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    
class Assignment(models.Model):
    platform = models.CharField(max_length=200)
    file = models.CharField(max_length=200)
    written_submission = models.TextField(blank=True, null=True)
    contact_method_email = models.CharField(max_length=200, blank=True, null=True)
    contact_method_slack = models.CharField(max_length=200, blank=True, null=True)
    contact_method_conveniote = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

class Notes(models.Model):
    notes = models.TextField(blank=True, null=True)
