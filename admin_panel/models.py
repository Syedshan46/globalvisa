from django.db import models

# Create your models here.
class Register(models.Model):
    reg_name = models.CharField(max_length=200)
    reg_pass = models.IntegerField()
    
    def __str__(self):
        return self.reg_user
