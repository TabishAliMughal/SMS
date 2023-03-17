from email import feedparser
from django.shortcuts import get_object_or_404, redirect, render
from School.S_School.models import School
from School.S_Record.models import ClassSection, Class, ClassSubjects , Session, Subject , SchoolDetail , SchoolAlbumImages , SchoolAlbumVideos , SchoolAnnouncements , SchoolFeeStructure , FeeTypes
from School.S_Record.forms import ManageClassSectionCreateForm, ManageClassCreateForm, ManageClassSubjectCreateForm , ManageSessionCreateForm, ManageSubjectCreateForm , ManageSchoolDetailCreateForm , ManageSchoolAlbumImagesCreateForm , ManageSchoolAlbumVideosCreateForm , ManageSchoolAnnouncementsCreateForm , ManageSchoolFeeStructureCreateForm 
from School.S_Students.models import Student , StudentStatus
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required
from .forms import ManageFeeTypeCreateForm



@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageFeeTypesListView(request):
    feetypes = []
    v = int('0')
    for i in FeeTypes.objects.all():
        v = v + 1
        feetypes.append({'pk' : v , 'name' : i.name })
    context = {
        'feetypes':feetypes,
    }
    return render(request,"S_Fee/FeeType/List.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageFeeTypesCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(FeeTypes , pk = pk)
    else:
        instance = None
    if request.method == "POST":
        form = ManageFeeTypeCreateForm(request.POST,instance=instance)
        form.save()
        return redirect('school_fee:fee_type_list')
    else:
        form = ManageFeeTypeCreateForm(instance=instance)
        context = {
            'form' : form ,
        }
        return render(request,"S_Fee/FeeType/Create.html",context)