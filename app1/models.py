from django.db import models
from django.utils import timezone
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
	    return self.title
		
class Contact(forms.Form):
    email = forms.EmailField(required=True)
    first = forms.CharField(required=True)
    last = forms.CharField(required=True)
# Create your models here.
