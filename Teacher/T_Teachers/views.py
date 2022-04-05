from django.shortcuts import render


def ManageTeacherProfileView(request):
    context = {

    }
    return render(request , 'T_Teacher/Profile.html',context)