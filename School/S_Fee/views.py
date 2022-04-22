from django.shortcuts import render , get_object_or_404
from School.S_Record.models import Class
from School.S_Students.models import StudentStatus
from .models import StudentFeeRecord
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageDueFeeView(request,_from=None,type=None,message=None,added=None,not_added=None):
    due_fee = []
    fee = []
    for i in StudentFeeRecord.objects.all().filter(status = "Due"):
        fee.append(i)
    for i in StudentFeeRecord.objects.all().filter(status = "PartialyPaid"):
        fee.append(i)
    for i in fee:
        i.current_class = StudentStatus.objects.get(student = i.student).current_class
        due_fee.append(i)
    if str(_from) == 'Student':
        message = message
        type = type
    elif str(_from) == 'Class':
        added = added
        not_added = not_added
    context = {
        'due_fee':due_fee,
        'message':message,
        'from':_from,
        'type':type,
        'added':added,
        'not_added':not_added,
    }
    return render(request ,'S_Fee/DueFeeList.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageDueFeeClassView(request):
    fee = []
    for i in Class.objects.all().order_by('serial'):
        due_fee = []
        for j in StudentFeeRecord.objects.all().filter(status = "Due"):
            try:
                status = get_object_or_404(StudentStatus , student = j.student , valid = "True" , current_class = i)
                j.current_class = status.current_class
                j.current_section = status.current_section
                j.created = status.created
                if int(j.current_class.pk) == int(i.pk):
                    due_fee.append(j)
            except:
                pass
        fee.append({'class':i,'due_fee':due_fee})
    context = {
        'fee':fee,
    }
    return render(request ,'S_Fee/DueFeeClass.html',context)
