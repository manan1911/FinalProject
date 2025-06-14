from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re

class CustomUser(AbstractUser):
    USER ={
        (1,'admin'),
        (2,'doc'),
        
    }
    user_type = models.CharField(choices=USER,max_length=50,default=1)

    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Specialization(models.Model):
    sname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sname
   
def validate_mobile(value):
    pattern = r'^\d{10}$'
    if not re.match(pattern, value):
        raise ValidationError('Enter a valid 10-digit mobile number.')

class DoctorReg(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
   
    # mobilenumber = models.CharField(max_length=10)
    mobilenumber = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\d{10}$', message='Enter a valid 10-digit mobile number')]
    )
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.admin:
            return f"{self.admin.first_name} {self.admin.last_name} - {self.mobilenumber}"
        else:
            return f"User not associated - {self.mobilenumber}"

class Appointment(models.Model):
    appointmentnumber = models.IntegerField(default=0)
    fullname = models.CharField(max_length=250)
    mobilenumber = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    date_of_appointment = models.CharField(max_length=250)
    time_of_appointment = models.CharField(max_length=250)
    doctor_id = models.ForeignKey(DoctorReg, on_delete=models.CASCADE)
    additional_msg = models.TextField(blank=True)
    remark = models.CharField(max_length=250,default=0)
    status = models.CharField(default=0,max_length=200)
    prescription=models.TextField(blank=True,default=0)
    recommendedtest=models.TextField(blank=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment #{self.appointmentnumber} - {self.fullname}"

class Page(models.Model):
    pagetitle = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    aboutus = models.TextField()
    email = models.EmailField(max_length=200)
    # mobilenumber = models.IntegerField(default=0)
    mobilenumber = models.IntegerField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pagetitle
 
