from django.db import models

# Create your models here.

class ClientModel(models.Model):
    client_name = models.CharField(max_length=100,unique=True)
    created_at = models.CharField(max_length=100,blank=True)
    created_by = models.CharField(max_length=100,blank=True)
    updated_by = models.CharField(max_length=100,blank=True)
    updated_at = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return self.client_name

class ProjectModel(models.Model):
    p_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    p_created_at = models.CharField(max_length=100,blank=True)
    p_created_by = models.CharField(max_length=100,blank=True)
    users_assign = models.TextField()

    def __str__(self):
        return self.p_name

class projectUserModel(models.Model):
    user = models.CharField(max_length=100)
    projects = models.CharField(max_length=200,blank=True)
    client_name = models.CharField(max_length=100,blank=True)
    record_id = models.CharField(max_length=100,blank=True)
    user_assign_names = models.CharField(max_length=100,blank=True)
    created_at = models.CharField(max_length=100,blank=True)
    created_by = models.CharField(max_length=100,blank=True)



    def __str__(self):
        return f"{self.projects}  , User : {self.user}"