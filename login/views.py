"""from django.http import HttpResponse







def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""

from django.http import HttpResponse
from django.template import loader
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Department, Employee
import sys
 
def index(request):
    template = loader.get_template('login/index.html')
    context = {
        'data': ['pawan','arti'],
    }
    return HttpResponse(template.render(context, request))

@login_required
def delete_user(request):
    if request.method == 'POST':
     form = DeleteEmpForm(request.POST)
     print("In emp delete\n")
     if form.is_valid():
      try:
       e = Employee.objects.get(name=form.cleaned_data['name'])
       print(e.name);
       e.delete()
       variables = RequestContext(request, { 'del_cont':"{0} deleted successfully".format(form.cleaned_data['name']) 
    })
       return render_to_response(
       'login/delete.html',variables,)
      except:
       data = "{0} does not exist".format(form.cleaned_data['name'])
       variables = RequestContext(request, { 'del_cont':data})
       return render_to_response('login/delete.html',variables,)  
     else:
       data = "Error in employee delete"
       variables = RequestContext(request, { 'del_cont':data}) 
       return render_to_response('login/delete.html',variables,)
      
    else:
       form = DeleteEmpForm()
       variables = RequestContext(request, {
       'form': form
       })
       return render_to_response(
       'login/delete_employee.html',variables,
       )
def delete_department(request):
    if request.method == 'POST':
     form = DeleteDepForm(request.POST)
     if form.is_valid():
      try:
       d = Department.objects.get(name=form.cleaned_data['name'])
       d.delete()
       variables = RequestContext(request, { 'del_cont':"{0} deleted successfully".format(form.cleaned_data['name'])
    })
       return render_to_response(
       'login/delete.html',variables,)
      except:
       data = "{0} does not exist".format(form.cleaned_data['name'])
       variables = RequestContext(request, { 'del_cont':data})
       return render_to_response('login/delete.html',variables,)
     else:
       data = "Error in employee delete"
       variables = RequestContext(request, { 'del_cont':data})
       return render_to_response('login/delete.html',variables,)

    else:
       form = DeleteDepForm()
       variables = RequestContext(request, {
       'form': form
       })
       return render_to_response(
       'login/delete_department.html',variables,
       )
        

@login_required
def add_user(request):
    if request.method == 'POST':
       form = EmployeeForm(request.POST)
       print(request.POST)
       if form.is_valid():
          d = Department.objects.get(name=form.cleaned_data['dep'])
          if d:
             e = Employee(name=form.cleaned_data['name'],date_of_joining=form.cleaned_data['doj'],dept=d)
             e.save()
             print("Name = {0} doj = {1} dep = {2}\n".format(form.cleaned_data['name'],form.cleaned_data['doj'],d.desc))
          
       return HttpResponseRedirect('/home/')
    else:
       form = EmployeeForm() 
    department_list = Department.objects.all()
    variables = RequestContext(request, {
    'form': form,'department_list':department_list
    })
    
    return render_to_response(
    'login/add_user.html',variables,
    )
@login_required
def add_department(request):
    print("In add department \n")
    if request.method == 'POST':
       form = DepartmentForm(request.POST)
       if form.is_valid():
          print("Name = {0} Desc = {1}\n".format(form.cleaned_data['name'],form.cleaned_data['desc']))
          d = Department(name=form.cleaned_data['name'],desc=form.cleaned_data['desc'])
          d.save()
       else:
         print("Form is not valid\n")
       return HttpResponseRedirect('/home/')
    else:
       form = DepartmentForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'login/add_department.html',variables,
    )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'login/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'login/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    employee_list = Employee.objects.all()
    department_list = Department.objects.all()
    return render_to_response(
    'login/home.html',
    { 'user': request.user ,'employee_list':employee_list, 'department_list':department_list}
    )
