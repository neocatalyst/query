from django.db import models
from django.core.exceptions import ValidationError

def validate_usn(value):
		if value != r"1RV[0-9]{2}[A-Z]{2}[0-9]{3}":
			raise ValidationError(u'invalid usn')
			
			
def validate_GPA(value):
		if ( int(value) > 10 ) | (int(value) < 0 )  :
			raise ValidationError(u'invalid GPA')
 

# Create your models here.
class Student(models.Model):
    USN = models.CharField(max_length=10, primary_key=True,validators=[validate_usn])
    Name = models.CharField(max_length=30)
    Branch = models.CharField(max_length=10)
    Year_of_admission = models.IntegerField()
    adm_choice = (('REG', 'Regular'), ('DIP', 'Diploma'),)
    Type_of_Admission = models.CharField(max_length=3, choices=adm_choice)

    def __unicode__(self):
        return u'%s \t %s' % (self.USN, self.Name)
        
    

class Subject(models.Model):
    Subject_code = models.CharField(max_length=6, primary_key=True)
    Subject_name = models.CharField(max_length=20)
    Credits = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % (self.Subject_code, self.Subject_name)


class GPA(models.Model):
    USN = models.ForeignKey(Student)
    Sem_no = models.IntegerField()
    SGPA = models.DecimalField(max_digits=4, decimal_places=2,validators=[validate_GPA])
    CGPA = models.DecimalField(max_digits=4, decimal_places=2,validators=[validate_GPA])

    def __unicode__(self):
        return u'%s has a CGPA of %s in %s sem' % (self.USN, str(self.CGPA),str(self.Sem_no))


class Subject_Grades(models.Model):
    USN = models.ForeignKey(Student)
    Sem_no = models.IntegerField()
    Subject_code = models.ForeignKey(Subject)
    res_choice = (('S', 'S'),
     ('A', 'A'),
     ('B', 'B'),
     ('C', 'C'),
     ('D', 'D'),
     ('E', 'E'),
     ('F', 'FAIL'),
     ('ab', 'ABSENT'),)
    Grade = models.CharField(max_length=2, choices=res_choice)
    type_choice = (('E', 'Even'), ('O', 'Odd'), ('FT', 'Fasttrack'),)
    Type = models.CharField(max_length=2, choices=type_choice)
    rem_choice = (('N', 'Normal'), ('M', 'Makeup'), ('R', 'Reval'),)
    Remark = models.CharField(max_length=1, choices=rem_choice)
    Attempts = models.IntegerField()

    def __unicode__(self):
        return u'%s scored %s in  %s' % (self.USN, self.Grade, self.Subject_code)


class Parent(models.Model):
    USN = models.ForeignKey(Student)
    Parent_name = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    Phone_no = models.BigIntegerField(max_length=10)
    email_id = models.CharField(max_length=30,verbose_name='email-id',blank=True)

    def __unicode__(self):
        return self.Parent_name
