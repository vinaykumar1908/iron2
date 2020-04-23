from django.db import models

# Create your models here.
class registerWheelRecievedJudw(models.Model):
    Date = models.DateTimeField(blank=True)
    TruckNo = models.CharField(max_length=12)
    BLC = models.IntegerField()
    BCN = models.IntegerField()
    ICF = models.IntegerField()
    Remark = models.TextField()
    def __str__(self):
        return str(self.Date)
class registerWheelDispatchedJudw(models.Model):
    Date = models.DateTimeField(blank=True)
    TruckNo = models.CharField(max_length=12)
    BLC = models.IntegerField()
    BCN = models.IntegerField()
    ICF = models.IntegerField()
    Remark = models.TextField()
    def __str__(self):
        return str(self.Date)
class registerHotAxle_Wagon(models.Model):
    DateDetached = models.DateTimeField(blank=True)
    Station = models.CharField(max_length=5)
    Section = models.CharField(max_length=5)
    WagonNumber = models.BigIntegerField()
    Railway = models.CharField(max_length=5)
    Class = models.CharField(max_length=5)
    TruckNo = models.CharField(max_length=12)
    WheelRecieveDate = models.DateTimeField()
    Remark = models.TextField()
    def __str__(self):
        return str(self.Date)