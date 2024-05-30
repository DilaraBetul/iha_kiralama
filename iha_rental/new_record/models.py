from django.db import models

class iha_models(models.Model):
    iha_Id=models.AutoField(primary_key=True)
    iha_name=models.CharField(max_length=200)
    iha_models=models.CharField(max_length=200)
    iha_feature=models.TextField()
    iha_startDate=models.DateField()
    iha_finishDate=models.DateField()
    iha_record= models.BooleanField(default=False)
     
