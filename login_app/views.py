from multiprocessing import context
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.shortcuts import  render, redirect
from .forms import NewUserForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate
# from django.contrib.auth import logout
from django.contrib.auth import login as logs

def register_page(request):
	if request.method =='POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			user = authenticate(email=email,password=password)
			login(request, user)
			messages.success(request, "Registration successful." )
			return render(request,"login_page.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	else:
		form = NewUserForm()
	return render (request,"register_page.html",{"form":form})


def login_page(request):
		if request.method == "POST":
				email = request.POST['email']
				password = request.POST['password']
				employee = authenticate(request,
				email = email,
				password = password
				)
				if employee is not None :
					login(request , employee)
					logged_employee = employee
					request.session['employee_id'] = logged_employee.id

					# request.employee.id = request.session['employee_id']
					print(logged_employee.id)
					print("hiiiiiiiiiii")
					return redirect('/services')
				else:
					messages.success(request,('there was an error logging in'))
					return redirect('/login')
			
		else:
			return render(request , 'login_page.html')

# def log_out(request):
#     logout(request)
#     return redirect('/login')
