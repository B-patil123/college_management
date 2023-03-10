from django.contrib import admin
from .models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
     list_per_page = 6
     list_display=['S_name','Reg_no','address','Taluka','District','pincode','State','MobileNo',]

admin.site.register(Student, StudentAdmin)
#admin.site.register(Demand)
#admin.site.register(Donor)

# Register your models here.
class AdmissionAdmin(admin.ModelAdmin):
    list_per_page = 6
    list_display=['S_name','Reg_no','clas','branch','year','date_of_admission','semester',]

admin.site.register(Admission, AdmissionAdmin)

class MarksAdmin(admin.ModelAdmin):
    list_per_page = 6
    list_display=['Reg_no','subject','marks','semester','year',]

admin.site.register(Marks,MarksAdmin)

class FeedbackAdmin(admin.ModelAdmin):
  list_per_page = 6
  
  list_display = ['reg_no','date','subject','feedback_message']

  def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Feedback,FeedbackAdmin)
