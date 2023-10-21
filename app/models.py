from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_name    = models.CharField(max_length=200)
    contact_email   = models.EmailField(max_length=200)
    contact_subject = models.CharField(max_length=200)
    contact_message = models.CharField(max_length=200)
    
    def __str__(self):
        return self.contact_name
