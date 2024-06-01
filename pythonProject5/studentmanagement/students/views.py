from django.shortcuts import render, redirect
from .models import Student, Faculty, Subject
from django.http import HttpResponse

# from json import dumps

def login(request):
    error = ""
    if request.method == 'POST':
        roll = request.POST['Roll_No']
        global st_id  # st_id is the id of the logged in student used in other templates (until logged out)
        st_id = roll
        error = ""
        pwd = request.POST['password']
        if Student.objects.filter(roll_no=roll, password=pwd):
            error += "success"

            return dashboard(request)
        else:
            error += "Try again"

    return render(request, 'login.html', {'error': error})


def loginAsFaculty(request):
    error = ""
    if request.method == 'POST':
        Faculty_Id = request.POST['Faculty_Id']
        global f_id  # f_id is the id of the logged in Faculty used in other templates (until logged out)
        f_id = Faculty_Id
        pwd = request.POST['password']
        if Faculty.objects.filter(fId=Faculty_Id, password=pwd):
            error = "success"
            s = "abc"
            return facultydashboard(request)
        else:
            error += "Try again"
    return render(request, 'loginAsfaculty.html', {'error': error})


def facultydashboard(request):
    if request.method == 'POST':
        roll = request.POST.get('rol')
        sCode = request.POST.get('subCode')
        A1 = request.POST.get('a1')
        A2 = request.POST.get('a2')
        if roll != None and Subject.objects.get(rollNo=roll, subjectCode=sCode):
            update = Subject.objects.get(rollNo=roll, subjectCode=sCode)
            update.assignment1 = A1
            update.assignment2 = A2
            update.total = int(A1) + int(A2)
            update.save()

    facultyitem = Faculty.objects.get(fId=f_id)
    subCode = facultyitem.subjectCode
    allStudent = Subject.objects.filter(subjectCode=subCode).order_by('rollNo')
    # for i in range(len(allStudent)):
    #     print(allStudent[i].classtest1)
    alldata = Subject()
    st = Student.objects.all()
    return render(request, 'facultydashboard.html',
                  {'data': alldata, 'allStudent': allStudent, 'student': st, 'faculty': facultyitem})
# Create your views here.

def export_students_to_excel(request):
    buffer = Student.export_to_excel()
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=students.xlsx'
    return response