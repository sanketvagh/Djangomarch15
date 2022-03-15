from django.db import models
from django.forms import ChoiceField
from datetime import date

# Create your models here.


class Inquiry(models.Model):
    inq_id = models.AutoField(primary_key=True)
    country=models.CharField(max_length=100,null=True)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    wmobile = models.CharField(max_length=12)
    email = models.EmailField(max_length=40)
    dob = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    gender = models.CharField(choices=(
        ('Male', 'Male'), ('Female', 'Female')), max_length=50, null=True, blank=True)
    isPassport = models.CharField(
        choices=(('yes', 'yes'), ('no', 'no')), max_length=50)
    address = models.TextField(max_length=300, default="some address")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    pincode = models.CharField(max_length=100, default="")
    instaid = models.CharField(max_length=100, default="")
    fbid = models.CharField(max_length=100, default="")
    marital_status = models.CharField(max_length=100, default="")
    no_child = models.CharField(max_length=100, default="")
    fdate1 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    tdate1 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    qual1 = models.CharField(max_length=100, default="")
    ctype1 = models.CharField(max_length=100, default="")
    marks1 = models.CharField(max_length=100, default="",null=True)
    school1 = models.CharField(max_length=100, default="")
    fdate2 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    tdate2 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    qual2 = models.CharField(max_length=100, default="")
    ctype2 = models.CharField(max_length=100, default="")
    marks2 = models.CharField(max_length=100, default="")
    school2 = models.CharField(max_length=100, default="")
    fdate3 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    tdate3 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    qual3 = models.CharField(max_length=100, default="")
    ctype3 = models.CharField(max_length=100, default="")
    marks3 = models.CharField(max_length=100, default="")
    school3 = models.CharField(max_length=100, default="")
    fdate4 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    tdate4 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    qual4 = models.CharField(max_length=100, default="")
    ctype4 = models.CharField(max_length=100, default="")
    marks4 = models.CharField(max_length=100, default="")
    school4 = models.CharField(max_length=100, default="")
    fdate5 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    tdate5 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    org1= models.CharField(max_length=100, default="")
    role1= models.CharField(max_length=100, default="")
    fdate6 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    tdate6 = models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    org2 = models.CharField(max_length=100, default="")
    role2= models.CharField(max_length=100, default="")
    fname=models.CharField(max_length=100, default="")
    occupation_type=models.CharField(max_length=100, default="")
    occupation_name = models.CharField(max_length=100, default="")
    english_test=models.CharField(choices=(('IELTS-General/Academy','IELTS-General/Academy'),('TOEFL','TOEFL'),('PTE','PTE')),max_length=100,null=True, blank=True)
    english_test_date=models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    lband=models.IntegerField(blank=True,default=0)
    rband=models.IntegerField(blank=True,default=0)
    wband=models.IntegerField(blank=True,default=0)
    sband=models.IntegerField(blank=True,default=0)
    oband=models.IntegerField(blank=True,default=0)
    General_test_date=models.DateField(blank=True,null=True,default=date(2022,1,1),help_text="write proper date")
    General_test_score=models.IntegerField(null=True,default=0)
    rejected=models.CharField(max_length=100, choices=(('Yes','Yes'),('No','No')),default='No')
    rejectedcountry = models.CharField(max_length=100, default="")
    ref = models.IntegerField(max_length=5,blank=True,null=True)
    ref=models.CharField(max_length=100, null=True)

    def __str__(self):
        fullname = self.firstname+self.lastname
        return fullname


class Smallinq(models.Model):
    country=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    mobile=models.CharField(max_length=100,null=True)
    wmobile=models.CharField(max_length=100,null=True)
    dob=models.DateField(null=True)
    gender=models.CharField(choices=(('Male','Male'),('Female','Female'),),max_length=20,null=True)
    ref=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name