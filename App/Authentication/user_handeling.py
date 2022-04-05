from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				for i in request.user.groups.all():
					if str(i) in allowed_roles:
						return view_func(request, *args, **kwargs)
			return redirect('main:not_authorized')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		if group == 'admin':
			return view_func(request, *args, **kwargs)
	return wrapper_function