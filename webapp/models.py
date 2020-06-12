from django.db import models

class CCDatails(models.Model):
    CreditNum=models.CharField(max_length=25)
    ExipryDate=models.CharField(max_length=5)
    CVV=models.IntegerField()
    Name=models.CharField(max_length=40)

    def __str__(self):
        return self.Name