from django.contrib import admin
from rquery.models import Student,Subject,Subject_Grades,GPA,Parent

class StudentAdmin(admin.ModelAdmin):
	list_display=('USN','Name','Branch','Year_of_admission','Type_of_Admission')
	search_fields=('USN','Name','Branch','Year_of_admission','Type_of_Admission')
	list_filter=('USN',)

class SubjectAdmin(admin.ModelAdmin):
	list_display=('Subject_code','Subject_name','Credits')
	search_fields=('Subject_code','Subject_name','Credits')
	
class Subject_GradesAdmin(admin.ModelAdmin):
	list_display=('USN','Sem_no','Subject_code','Grade','Type','Remark','Attempts')
	search_fields=('USN','Sem_no','Subject_code','Grade','Type','Remark','Attempts')
	
class GPAAdmin(admin.ModelAdmin):
	list_display=('USN','Sem_no','SGPA','CGPA')
	search_fields=('USN','Sem_no','SGPA','CGPA')
	
class ParentAdmin(admin.ModelAdmin):
	list_display=('USN','Parent_name','Address','Phone_no','email_id')
	search_fields=('USN','Parent_name','Address','Phone_no','email_id')
	



admin.site.register(Student,StudentAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Subject_Grades,Subject_GradesAdmin)
admin.site.register(GPA,GPAAdmin)
admin.site.register(Parent,ParentAdmin)
