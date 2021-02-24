from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from crud.models import Empolyee
# Import Datetime
from datetime import datetime

# Create your views here.

def home(request):
    data = Empolyee.objects.all()
    param = {'employees':data}
    return render(request, 'index.html', param)

def login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.info(request, 'Welcome!')
                return redirect('/')

            else:
                messages.info(request, 'Invailid Username or Password')
                return redirect('/login') 

        else:
            return render(request, 'login.html')
    else:
        messages.info(request, 'Already Login')
        return redirect('/')                   

def register(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            if User.objects.filter(username=email).exists():
                messages.info(request, 'Already Registered')
                return redirect('/signup')

            else:    
                user = User.objects.create_user(username = email, password = password, email = email, first_name = name)
                user.save()
                print('User added')
                messages.info(request, 'Account Created Successfully')
                return redirect('/login')

        else:
            return render(request, 'register.html')
    else:
        return redirect('/logout')          

def logout(request):
    auth.logout(request)
    messages.info(request, 'Thank You, Come Again')
    return redirect('/login')

@login_required(login_url='/login')
def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        dob = request.POST['date']

        newEmployee = Empolyee(emp_name=name, emp_email=email, emp_contact=contact, emp_gender=gender, emp_dob=dob)
        newEmployee.save()

        messages.info(request,'Employee Added')
        return redirect('/')

    else:
        return render(request, 'create.html')

@login_required(login_url='/login')
def update(request, id):
    emp = Empolyee.objects.filter(emp_id=id)
    myDate = emp[0].emp_dob
    formatedDate = myDate.strftime("%Y-%m-%d")    
    print('Date is ', formatedDate) 
    # print('Parsed date is ', parsed_date) 
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        dob = request.POST['date']
        
        emp.update(emp_name = name, emp_email = email, emp_contact = contact, emp_gender = gender, emp_dob = dob)
        
        messages.info(request,'Employee Data Updated')
        return redirect('/')

    else:
        param={'employees':emp, 'date':formatedDate}
        return render(request, 'update.html', param)

@login_required(login_url='/login')
def delete(request, id):
    emp = Empolyee.objects.filter(emp_id=id)
    emp.delete()
    messages.info(request, 'Employee Record Deleted')
    return redirect('/')