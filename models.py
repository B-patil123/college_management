from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


   

Branches=(
    ('Information Technology','Information Technology'),
    ('Mechnical','Mechnical'),
    ('Textile','Textile'),
    ('Chemicals','Chemicals')
)


SEMESTER=(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
)

classes=(
     ('FY', 'FY'),
     ('SY', 'SY'),
   
     ('TY', 'TY'),
     ('Btech', 'Btech')
   
)

SUBJECTS=(
    ('DM','DM'),
    ('DSA','DSA'),
    ('CPP','CPP'),
    ('HVPE','HVPE')
)

class Student(models.Model):
  S_name=models.CharField(max_length=20,blank=True,null=True,default="Ankita")
  Reg_no=models.CharField(max_length=20,blank=True,null=True,default="2021BIT505")
  address=models.CharField(max_length=50,blank=True,null=True,default="khanapur nagar parbhani")
  Taluka=models.CharField(max_length=50,blank=True,null=True,default="Parbhani")
  District=models.CharField(max_length=50,blank=True,null=True,default="Parbhani")
  pincode=models.IntegerField(blank=True,null=True)
  State=models.CharField(max_length=50,blank=True,null=True,default="Maharashtra")
  MobileNo=models.IntegerField(blank=True,null=True,default="9145111609")
  #photo=models.ImageField(upload_to='uploads')

def str(self):
    return str(self.Reg_no) 
    return str(self.S_name)


class Admission(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)   
 Reg_no=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)  
 S_name=models.CharField(max_length=20,blank=True,null=True,default="Ankita")
 clas=models.CharField(max_length=20,blank=True,null=True,choices=classes)
 branch=models.CharField(max_length=100,blank=True,null=True,choices=Branches)
 year=models.IntegerField(blank=True,null=True,default="2022")
 date_of_admission=models.DateField(blank=True,null=True)
 semester=models.IntegerField(blank=True,null=True,choices=SEMESTER)

def str(self):
    return str(self.Reg_no) 
    return str(self.S_name)



class Marks(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
 Reg_no=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
 subject=models.CharField(max_length=100,blank=True,null=True,choices=SUBJECTS)
 marks=models.IntegerField(blank=True,null=True,default="100")
 semester=models.IntegerField(blank=True,null=True,choices=SEMESTER)
 year=models.IntegerField(blank=True,null=True,default="2022")
 
def str(self):
    return str(self.Reg_no) 
    #return str(self.S_name)



 
class Feedback(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
  reg_no = models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
  date =models.DateField()
  subject =models.CharField(max_length=20,blank=True,null=True)
  feedback_message = models.CharField(max_length=200,blank=True,null=True)

def str(self):
    return str(self.Reg_no) 
    #return str(self.S_name)
