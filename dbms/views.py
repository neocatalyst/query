from django.http import HttpResponse
from django.shortcuts import render_to_response
from rquery.models import Student,Subject,Subject_Grades,GPA,Parent
from collections import Counter


def gradess(s):
	year=s[3]
	year1=str(int(year)+1)
	grad=s[5]
	sub=s[8]
	students2=Subject_Grades.objects.filter(USN__Year_of_admission=year,Grade=grad,Subject_code=sub,USN__Type_of_Admission='REG')	
	students1=Subject_Grades.objects.filter(USN__Year_of_admission=year1,Grade=grad,Subject_code=sub,USN__Type_of_Admission='DIP')	
	students = list(students2) + list(students1)
	return students

def noft(s):
	year=s[3]
	year1=str(int(year)+1)
	listta=Student.objects.filter(Year_of_admission=year,Type_of_Admission='REG')
	listtb=Student.objects.filter(Year_of_admission=year1,Type_of_Admission='DIP')
	listt= list(listta)+list(listtb)
	listfta=Subject_Grades.objects.filter(USN__Year_of_admission=year,Type='FT',USN__Type_of_Admission='REG')
	listftb=Subject_Grades.objects.filter(USN__Year_of_admission=year1,Type='FT',USN__Type_of_Admission='DIP')
	listft=list(listfta)+list(listftb)
	listt1=[]
	listft1=[]
	for i in listt:
		listt1.append(i.USN)
	for j in listft:
		listft1.append(j.USN.USN)
		
	for x in listft1:
		if x in listt1:
			listt1.remove(x)
	list2=Student.objects.filter(USN__in=listt1)
	return list2
	

def fts(s):
	year=s[3]
	year1=str(int(year)+1)
	num=s[5]
	listfta=Subject_Grades.objects.filter(USN__Year_of_admission=year,Type='FT',USN__Type_of_Admission='REG')
	listftb=Subject_Grades.objects.filter(USN__Year_of_admission=year1,Type='FT',USN__Type_of_Admission='DIP')
	listft= list(listfta)+list(listftb)
	listft1=[]
	listft2=[]
	for j in listft:
		listft1.append(j.USN.USN)
	for i in Counter(listft1):
		if Counter(listft1)[i]==int(num):
			listft2.append(i)
	list2=Student.objects.filter(USN__in=listft2)
	return list2

def cgpass(s):
	year=s[3]
	year1=str(int(year)+1)
	l=s[6]
	num=s[8]
	sem=s[11]
	if l=='less':
		students=GPA.objects.filter(USN__Year_of_admission=year,CGPA__lt=num,Sem_no=sem,USN__Type_of_Admission='REG')|GPA.objects.filter(USN__Year_of_admission=year1,CGPA__lt=num,Sem_no=sem,USN__Type_of_Admission='DIP')
		return students	
	else:
		students=GPA.objects.filter(USN__Year_of_admission=year,CGPA__gte=num,Sem_no=sem,USN__Type_of_Admission='REG')|GPA.objects.filter(USN__Year_of_admission=year1,CGPA__gte=num,Sem_no=sem,USN__Type_of_Admission='DIP')		
		return students		
	

def sgpass(s):
	year=s[3]
	year1=str(int(year)+1)
	l=s[6]
	num=s[8]
	sem=s[11]
	if l=='less':
		students=GPA.objects.filter(USN__Year_of_admission=year,SGPA__lt=num,Sem_no=sem,USN__Type_of_Admission='REG')|GPA.objects.filter(USN__Year_of_admission=year1,SGPA__lt=num,Sem_no=sem,USN__Type_of_Admission='DIP')	
	else:
		students=GPA.objects.filter(USN__Year_of_admission=year,SGPA__gte=num,Sem_no=sem,USN__Type_of_Admission='REG')|GPA.objects.filter(USN__Year_of_admission=year1,SGPA__gte=num,Sem_no=sem,USN__Type_of_Admission='DIP')
	return students			


def rank(s):
	year=s[3]
	year1=str(int(year)+1)
	sem=s[7]
	students=(GPA.objects.filter(USN__Year_of_admission=year,Sem_no=sem,USN__Type_of_Admission='REG')|GPA.objects.filter(USN__Year_of_admission=year1,Sem_no=sem,USN__Type_of_Admission='DIP')).order_by('-CGPA')
	return students	


def clear(s):
	year=s[3]
	year1=str(int(year)+1)
	sems=int(s[7])
	sem1=2*sems
	sem2=sem1-1
	listta=Student.objects.filter(Year_of_admission=year,Type_of_Admission='REG')
	listtb=Student.objects.filter(Year_of_admission=year1,Type_of_Admission='DIP')
	listt= list(listta)+list(listtb)
	listfta=(Subject_Grades.objects.filter(USN__Year_of_admission=year,Type='FT',USN__Type_of_Admission='REG',Sem_no=sem1)|Subject_Grades.objects.filter(USN__Year_of_admission=year,Type='FT',USN__Type_of_Admission='REG',Sem_no=sem2))
	listftb=(Subject_Grades.objects.filter(USN__Year_of_admission=year1,Type='FT',USN__Type_of_Admission='DIP',Sem_no=sem1)|Subject_Grades.objects.filter(USN__Year_of_admission=year1,Type='FT',USN__Type_of_Admission='DIP',Sem_no=sem1))
	listft=list(listfta)+list(listftb)
	listt1=[]
	listft1=[]
	for i in listt:
		listt1.append(i.USN)
	for j in listft:
		listft1.append(j.USN.USN)
		
	for x in listft1:
		if x in listt1:
			listt1.remove(x)
	list2=Student.objects.filter(USN__in=listt1)
	return list2
	


def home(request):  
	return render_to_response('search.html')

def display_meta(request):
	values=request.META.items()
	values.sort()
	html=[]
	for k,v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
	return render_to_response('search.html')


def search(request):
	error=[]
	if 'q' in request.GET:
		q=request.GET['q']
		if not q:
			error.append("Please enter a search term")
		else:
			s=q.split()
			if 'grade' in s:
				students=gradess(s)
			elif 'CGPA' in s:
				students=cgpass(s)
			elif 'SGPA' in s:
				students=sgpass(s)
			elif 'no' in s and 'fasttrack' in s:
				students=noft(s)
				return render_to_response('search_results2.html',{'students':students,'query':q})
			elif 'rank' in s:
				students=rank(s)
			elif 'fasttrack' in s:
				students=fts(s)	
			elif 'cleared' in s:
				students=clear(s)
				return render_to_response('search_results2.html',{'students':students,'query':q})
			else:
				error.append("Not able to undertand the command , Please see Help")
				return render_to_response('search.html',{'error':error})
			return render_to_response('search_results.html',{'students':students,'query':q})
	return render_to_response('search.html',{'error':error}) 
