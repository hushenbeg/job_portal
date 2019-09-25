from django.db import models
# from cgi import maxlen

# Create your models here.
class HydJob(models.Model):
   
    posting_date = models.DateField()
    job_title = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    eligibility = models.CharField(max_length=64)
    last_date = models.DateField()
    more_information = models.CharField(max_length=64)

class PuneJob(models.Model):
    posting_date = models.DateField()
    job_title = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    eligibility = models.CharField(max_length=64)
    last_date = models.DateField()
    more_information = models.CharField(max_length=64)


class BangaloreJob(models.Model):
    posting_date = models.DateField()
    job_title = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    eligibility = models.CharField(max_length=64)
    last_date = models.DateField()
    more_information = models.CharField(max_length=64)

class ChennaiJob(models.Model):
    posting_date = models.DateField()
    job_title = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    eligibility = models.CharField(max_length=64)
    last_date = models.DateField()
    more_information = models.CharField(max_length=64)
