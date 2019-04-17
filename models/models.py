from django.db import models
from django.utils.timezone import now
# Create your models here.
class Country(models.Model):
      id   = models.AutoField(primary_key=True)
      name = models.CharField(max_length=500)


class  State(models.Model):
       id   = models.AutoField(primary_key=True)
       name = models.CharField(max_length=500)
       cid  = models.IntegerField()


class  Town(models.Model):
       id   = models.AutoField(primary_key=True)
       name = models.CharField(max_length=500)
       sid  = models.IntegerField()


class  Source(models.Model):
       id   = models.AutoField(primary_key=True)
       name = models.CharField(max_length=200)
       url  = models.TextField()
       cid  = models.IntegerField()  
       status = models.IntegerField()


class  Articles(models.Model):
       id   = models.AutoField(primary_key=True)
       title = models.CharField(max_length=255)
       summary = models.TextField()
       shortdesc = models.TextField()
       content = models.TextField()
       sid  = models.IntegerField()
       status = models.IntegerField()
       author = models.CharField(max_length=200)
       pubdate =  models.DateTimeField(default=now)


class Profile(models.Model):
       
      id = models.AutoField(primary_key=True)
      uid = models.IntegerField()
      firstname = models.CharField(max_length=100)
      lastname = models.CharField(max_length=100)
      othername = models.CharField(max_length=100)
      email = models.EmailField(max_length=100)
      telephone = models.CharField(max_length=100)
      address = models.CharField(max_length=100)
      address2 = models.CharField(max_length=100)
      city = models.IntegerField()
      state = models.IntegerField()
      country = models.IntegerField()
      postal = models.CharField(max_length=20)
      createdate = models.DateTimeField(default=now)



class User(models.Model):
    
      id = models.AutoField(primary_key=True)
      username = models.CharField(max_length=10)
      password = models.CharField(max_length=200)
      secret = models.CharField(max_length=200)
      isemailverified = models.IntegerField()
      isphoneverified  = models.IntegerField()
      status = models.IntegerField()
      createdate = models.DateTimeField(default=now)


class Admin(models.Model):
       id            = models.AutoField(primary_key=True)
       username      = models.CharField(max_length=20)
       password      = models.CharField(max_length=200)
       secret        = models.CharField(max_length=20)
       admintype     = models.IntegerField()
       status        = models.IntegerField()
       createdate    = models.DateTimeField(default=now)


class AdminType(models.Model):
       id            = models.AutoField(primary_key=True)
       name      = models.CharField(max_length=20)

       