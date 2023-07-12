from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def display_student(request):
    SO = Student_Form()
    d={'SO':SO}
    if request.method=='POST':
        SFD=Student_Form(request.POST)
        if SFD.is_valid():
            # name=SU.cleaned_data['name']
            # return HttpResponse(str(name))
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('<center><h1 style="color:blue;">data is invalid </h1></center>')
    return render(request,'display_student.html',d)