from django.shortcuts import render
from .models import Student,Marks

def index(request):
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def branches(request):
    return render(request, 'branches.html')

def cse(request):
    return render(request, 'cse.html')

def it(request):
    return render(request, 'it.html')

def mech(request):
    return render(request, 'mech.html')

def eee(request):
    return render(request, 'eee.html')

def ece(request):
    return render(request, 'ece.html')

def result_search(request):
    return render(request,'result_search.html')

def get_result(request):
    if request.method == "POST":
        reg_no = request.POST.get('regno')
        student_qs=Student.objects.filter(reg_no=reg_no)
        if student_qs:
            student=Student.objects.get(reg_no=reg_no)
            marks_qs=Marks.objects.filter(student=student)

            SecuredScore=0
            for m in marks_qs:
                SecuredScore=SecuredScore+m.marks
            
            totalMarks=len(marks_qs)*100
            percentage=round((SecuredScore/totalMarks)*100,2)

            if percentage>=95 :
                grade='S'
            elif percentage>=90 and percentage<95:
                grade='A'
            elif percentage>=80 and percentage<90:
                grade='B'
            elif percentage>=70 and percentage<80:
                grade='C'
            elif percentage>=60 and percentage<70:
                grade='D'
            elif percentage>=50 and percentage<60:
                grade='E'
            else:
                grade='F'
            return render(request,'result_display.html',
                          {'student':student,'marks_qs':marks_qs,'SecuredScore':SecuredScore,
                           'totalMarks':totalMarks,'percentage':percentage,'grade':grade})
        else:
            return render(request,'result_search.html',{'message':'Invalid Register Number'})

            




