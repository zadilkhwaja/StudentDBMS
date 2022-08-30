from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import pandas as pd
from .models import StudentData

df = pd.read_excel('student.xlsx')  # to dataframe
p = df.to_dict('records')  # to dict

mem = [StudentData(
        StudentName = record['StudentName'],
        CollegeName = record['CollegeName'],
        RollNo = record['RollNo'],
        Language = record['Language'],
      ) for record in p]

StudentData.objects.bulk_create(mem)

def index(request):
    q = StudentData.objects.all().values()
    template = loader.get_template('index.html')
    context = {'q': q,}
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  w = request.POST['firstName']
  x = request.POST['CollegeName']
  y = request.POST['RollNumber']
  z = request.POST['Skill']
  q = StudentData(StudentName=w, CollegeName=x, RollNo=y, Language=z)
  q.save()
  m = pd.DataFrame(list(StudentData.objects.all().values()))
  m.to_excel("student.xlsx")
  return HttpResponseRedirect(reverse('index'))
