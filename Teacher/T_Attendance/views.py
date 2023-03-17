from datetime import datetime
from django.shortcuts import render , get_object_or_404
from School.S_Teachers.models import Teacher
from django.contrib.auth.models import Group , User
from django.contrib.auth import authenticate
from Teacher.T_Attendance.forms import ManageTeacherAttendanceCaptureForm
from Teacher.T_Attendance.models import TeacherAttendance
from School.S_Record.models import Class
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required
import pytz


@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageTeacherAttendanceView(request):
    present = []
    absent = []
    for v in TeacherAttendance.objects.all():
        if (request.POST.get('date') if request.POST.get('date') else str(datetime.today().date())) == str(v.capture_datetime.date()):
            present.append(v)
    for i in Teacher.objects.all():
        if i.pk not in [k.teacher.pk for k in present]:
            absent.append(i)
    context = {
        'present' : present ,
        'absent' : absent ,
    }
    return render(request,'T_Attendance/Detail.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageTeacherAttendanceCaptureView(request):
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
            context['message'] = 'Teacher Not Found'
        if user != '':
            try:
                teacher = get_object_or_404(Teacher , user = user)
                try :
                    attendance = get_object_or_404(TeacherAttendance , teacher = teacher , date_of_attendance = datetime.today())
                    context['status'] = 'already'
                    context['message'] = 'Attendance Already Saved For Teacher {} At {}'.format(attendance.teacher,str(attendance.capture_datetime.time())[0:8])
                except:
                    pak = pytz.timezone("Asia/Karachi") 
                    timeInNewYork = datetime.now(pak)
                    currentTimeInNewYork = timeInNewYork
                    form = ManageTeacherAttendanceCaptureForm({
                        'teacher' : teacher ,
                        'date_of_attendance' : datetime.today() ,
                        'capture_datetime' : datetime.now() ,
                    })
                    form.save()
                    context['status'] = 'ok'
                    context['message'] = 'Attendance Saved For Teacher {} Via {}'.format(teacher,k)
            except:
                context['status'] = 'error'
                context['message'] = 'Teacher Not Found'
        return render(request , "T_Attendance/Capture.html" , context)
    else:
        return render(request , "T_Attendance/Capture.html")