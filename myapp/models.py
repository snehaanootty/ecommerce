from django.db import models
from django.contrib.auth.models import User

class MobileStore(models.Model):
    name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    model=models.CharField(max_length=200)
    rate=models.CharField(max_length=200)
    storage=models.CharField(max_length=200)
    pic=models.ImageField(upload_to="images",null=True,blank=True)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name
        

