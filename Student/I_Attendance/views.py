from datetime import datetime
from django.shortcuts import render , get_object_or_404
from School.S_Students.models import Student, StudentStatus
from django.contrib.auth.models import Group , User
from django.contrib.auth import authenticate
from Student.I_Attendance.forms import ManageStudentAttendanceCaptureForm
from Student.I_Attendance.models import StudentAttendance
from School.S_Record.models import Class
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageStudentAttendanceView(request):
    classes = Class.objects.all()
    attendance = []
    present_students = []
    absent_students = []
    for i in range(1,32):
        students = len(Student.objects.all())
        present = '0'
        absent = '0'
        date = str(datetime.today().date())[0:-2] + f"{i:02}"
        try:
            for j in StudentAttendance.objects.all().filter(date_of_attendance = date ):
                # print(i.date_of_attendance)
                present = int(present) + 1
        except:
            pass
        present_students.append({'date' : date , 'total' : present})
        absent_students.append({'date' : date , 'total' : int(students) - int(present)})

    attendance.append({ 'present' : present_students })
    attendance.append({ 'absent' : absent_students })
    date = datetime.today().date()
    context = {
        'attendance' : attendance ,
        'classes' : classes ,
        'date' : date ,
    }
    return render(request , 'I_Attendance/View/Select.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageStudentAttendanceViaDateView(request):
    attendance = []
    for i in Class.objects.all():
        present_students = []
        absent_students = []
        for j in StudentAttendance.objects.all().filter(date_of_attendance = request.POST.get('date')):
            student_status = get_object_or_404(StudentStatus , student = j.student , valid = True)
            if str(student_status.current_class.pk) == str(i.pk):
                present_students.append(j)
        attendance.append({'class' : i , 'students' : present_students , 'total' : len(present_students)})
    date = request.POST.get('date')
    context = {
        'date' : date ,
        'attendance' : attendance ,
    }
    return render(request , 'I_Attendance/View/ViaDate.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageStudentAttendanceViaClassView(request,pk):
    clas = get_object_or_404(Class , pk = pk)
    attendance = []
    for i in range(1,32):
        students = []
        date = str(datetime.today().date())[0:-2] + f"{i:02}"
        try:
            for j in StudentAttendance.objects.all().filter(date_of_attendance = date ):
                if str(get_object_or_404(StudentStatus , student = j.student.pk).current_class.pk) == str(clas.pk):
                    students.append(j.student)
        except:
            pass
        attendance.append({'date' : date , 'students' : students , 'total' : len(students)})
    context = {
        'clas' : clas ,
        'attendance' : attendance ,
    }
    return render(request , 'I_Attendance/View/ViaClass.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageStudentAttendanceCaptureView(request):
    if request.method == 'POST':
        context = {}
        if request.POST.get('qr'):
            LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}:"|<>?,./;[]=- '+"'"
            def decrypt(message, key):
                decrypted = ''
                for i in message.split(','):
                    i = int(i) - int(key)
                    decrypted += str(LETTERS[i])
                return decrypted
            qr = request.POST.get('qr')
            user = get_object_or_404(User , username = decrypt(qr, '317'))
            k = 'QR Code'
        elif authenticate(request, username=request.POST.get('username'), password=request.POST.get('password')):
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            k = 'User ID'
        else:
            user = ''
            context['status'] = 'error'
            context['message'] = 'Student Not Found'
        if user != '':
            try:
                student = get_object_or_404(Student , user = user)
                try :
                    attendance = get_object_or_404(StudentAttendance , student = student , date_of_attendance = datetime.today())
                    context['status'] = 'already'
                    context['message'] = 'Attendance Already Saved For Student {} At {}'.format(attendance.student,str(attendance.capture_datetime.time())[0:8])
                except:
                    form = ManageStudentAttendanceCaptureForm({
                        'student' : student ,
                        'date_of_attendance' : datetime.today() ,
                        'capture_datetime' : datetime.now() ,
                    })
                    form.save()
                    context['status'] = 'ok'
                    context['message'] = 'Attendance Saved For Student {} Via {}'.format(student,k)
            except:
                context['status'] = 'error'
                context['message'] = 'Student Not Found'
        return render(request , "I_Attendance/Capture.html" , context)
    else:
        return render(request , "I_Attendance/Capture.html")