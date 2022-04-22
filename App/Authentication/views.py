from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group , User
from .forms import CreateUserForm
from django.contrib import messages
from School.S_School.models import Domain, School
from School.S_Students.models import Student
from tenant_schemas.utils import tenant_context

def HandleUser(request):
	groups = [i.get('name') for i in request.user.groups.values('name')]
	request.session['group'] = groups
	request.session.save()
	try:
		site = request.META['HTTP_HOST']
		school = get_object_or_404(School , schema_name = site.split(".")[0])
		request.session['school'] = {
			'pk' : school.pk ,
			'short_name' : school.short_name ,
			'full_name' : school.full_name ,
			'principal_name' : school.principal_name ,
			'active' : school.active ,
		}
		request.session.save()
	except:
		pass


def loginPage(request):
	path = '/'
	if request.method == 'POST':
		try:
			school = request.META['HTTP_HOST'].split(".")[0]
			tenant = get_object_or_404(School , schema_name = school)
		except:
			tenant = get_object_or_404(School , schema_name = "public")
		with tenant_context(tenant):
			qr = request.POST.get('qr')
			try:
				user = get_object_or_404(User , password = qr)
			except:
				username = request.POST.get('username')
				password =request.POST.get('password')
				user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				HandleUser(request)
				return HttpResponseRedirect(path)
			else:
				return redirect('main:main','rejected')
	else:
		return HttpResponseRedirect(path)

def logoutUser(request):
	logout(request)
	return redirect('main:main')

# @admin_only
# @login_required(login_url='main_login')
# @allowed_users(allowed_roles=['admin'])