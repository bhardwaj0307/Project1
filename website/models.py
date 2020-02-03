from django.db import models

# Create your models here.
class userLogin(models.Model):
    id=models.AutoField(primary_key=True)
    empid=models.IntegerField(default=1,unique=True)
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    is_usertype=models.CharField(max_length=100,default="")


    class Meta:
        db_table="login"

     
    def __str__(self):
        return self.username    
        

class addProject(models.Model):
    pid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    pname=models.CharField(max_length=100)
    pdes=models.CharField(max_length=100)
    cdetail=models.CharField(max_length=100)
    pdeadline=models.DateField()
    pstartdate=models.DateField()
    pmanagedby=models.CharField(max_length=100)
    pcontract=models.CharField(max_length=100)
    pstatus=models.CharField(max_length=100)


    class Meta:
        db_table="Project"

     
    def __str__(self):
        return self.pname
class addtask(models.Model):
    
    Tid=models.AutoField(primary_key=True)
    Tpname=models.ForeignKey(addProject,on_delete=models.CASCADE,default="")
    Ttitle=models.CharField(max_length=100)
    Pid=models.IntegerField()
    Tstatus=models.CharField(max_length=100)
    choice= (
    (1, ("Java")),
    (2, ("Python")),
    (3, ("Php")),
    (4, ("Wordpress")),
    (5, ("NodeJs")))
    Ttechnology=models.IntegerField(choices=choice)
    Tassignedto=models.CharField(max_length=100)
    Tassginedby=models.CharField(max_length=100)
    Tassigneddata=models.CharField(max_length=100)
    Tdeadline=models.DateField()

    class Meta:
        db_table="Task"

     
    def __str__(self):
        return self.Ttitle