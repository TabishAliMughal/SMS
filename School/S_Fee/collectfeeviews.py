from datetime import datetime
from django.shortcuts import redirect, render , get_object_or_404
import urllib
from School.S_School.models import School
from School.S_Students.models import Student
from .models import StudentFeeRecord
from .forms import ManageStudentFeeRecordCreateForm
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required


@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageCreateReceiptView(request,fee):
    fee = fee.replace('fee=','').split('&')
    receipt = []
    total_amount_paid = int('0')
    date = datetime.today()
    student = ""
    url = request.META['HTTP_HOST']
    for i in fee:
        record = get_object_or_404(StudentFeeRecord , pk = i)
        if str(record.paid_amount) != "0":
            receipt.append({
                'student' : record.student ,
                'month' : record.month ,
                'paid_date' : str(record.paid_date.date()) ,
                'fee_type' : record.fee.fee_type.name ,
                'fee' : record.fee.fee ,
                'paid_amount' : record.paid_amount ,
                'status' : record.status ,
            })
        student = record.student
        total_amount_paid = total_amount_paid + record.paid_amount
    context = {
        'receipt':receipt,
        'date':date,
        'url':url,
        'student':student,
        'user':request.user,
        'total_ammount_paid':total_amount_paid,
        'school':get_object_or_404(School,pk = request.session.get('school').get('pk')),
    }
    return render(request,'S_Fee/Receipt.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageFeeCollectView(request):
    if request.method == 'POST':
        try:
            student = get_object_or_404(Student , gr_number = int(request.POST.get("student")))
            return redirect('school_fee:student_due_fee_collect_bulk',student.pk)
        except:
            context = {
                'message': "Not Found",
                'gr': request.POST.get("student")
            }
            return render(request ,'S_Fee/CollectFee.html',context)
    else:
        context = {
        }
        return render(request ,'S_Fee/Collect/Fee.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageStudentFeeCollectView(request,pk):
    fee = get_object_or_404(StudentFeeRecord,pk = pk)
    if request.method == 'POST':
        fee.paid_amount = int(request.POST.get('paid_amount')) + (fee.paid_amount or 0)
        if int(fee.fee.fee) == int(fee.paid_amount):
            fee.status = 'Paid'
        else:
            fee.status = 'PartialyPaid'
        fee.paid_date = datetime.today()
        saved_fee = []
        saved_fee.append(fee.pk)
        fee.save()
        if str(request.POST.get('receipt')) == 'on':
            data = (urllib.parse.urlencode({'fee':saved_fee}, True))
            return redirect('school_fee:fee_receipt',data)
        else:
            return redirect('school_fee:due_fee_list')
    else:
        fee = get_object_or_404(StudentFeeRecord,pk = pk)
        if fee.paid_amount:
            fee.amount_to_pay = int(fee.fee.fee - fee.paid_amount)
        else:
            fee.amount_to_pay = int(fee.fee.fee)
        form = ManageStudentFeeRecordCreateForm(instance = fee)
        date = str(datetime.today().date())
        context = {
            'fee':fee,
            'form':form,
            'date':date
        }
        return render(request ,'S_Fee/Collect/StudentFee.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageStudentBulkFeeCollectView(request,pk):
    student = get_object_or_404(Student , pk = pk)
    if request.method == 'POST':
        fee = []
        for i in StudentFeeRecord.objects.all().filter(student = student , status = ("Due")).order_by("pk"):
            fee.append(i)
        for i in StudentFeeRecord.objects.all().filter(student = student , status = ("PartialyPaid")).order_by("pk"):
            fee.append(i)
        saved_fee = []
        for i in fee:
            i.paid_amount = int(request.POST.get(str(i.pk)) or 0) + (i.paid_amount or 0)
            if int(i.fee.fee) == int(i.paid_amount):
                i.status = 'Paid'
            else:
                i.status = 'PartialyPaid'
            i.paid_date = datetime.today()
            saved_fee.append(i.pk)
            i.save()
        if str(request.POST.get('receipt')) == 'on':
            data = (urllib.parse.urlencode({'fee':saved_fee}, True))
            return redirect('school_fee:fee_receipt',data)
        else:
            return redirect('school_fee:due_fee_list')
    else:
        fee = []
        records = []
        for i in StudentFeeRecord.objects.all().filter(student = student , status = ("Due")).order_by("pk"):
            records.append(i)
        for i in StudentFeeRecord.objects.all().filter(student = student , status = ("PartialyPaid")).order_by("pk"):
            records.append(i)
        for i in records:
            get_object_or_404(StudentFeeRecord, pk = i.pk)
            if i.paid_amount:
                i.amount_to_pay = i.fee.fee - i.paid_amount
            else:
                i.amount_to_pay = i.fee.fee
            fee.append(i)
        date = str(datetime.today().date())
        context = {
            'fee':fee,
            'student':student,
            'date':date
        }
        return render(request ,'S_Fee/Collect/BulkFee.html',context)
