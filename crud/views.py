from django.shortcuts import render, redirect 
#authentication
from django.contrib.auth.models import User, auth 
#Django message
from django.contrib import messages  
 #decorator to check authentication
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
#importing employee model
from crud.models import Empolyee  
# Import Datetime
from datetime import datetime

# Create your views here.

# Function for home/Index Page 
def home(request):
    data = Empolyee.objects.all()
    # Creating dictionary of employee
    param = {'employees':data}
    # Send data data to frontend
    return render(request, 'index.html', param)

# Function to authenticate User
def login(request):
    if request.user.is_anonymous:
        # If request come with data 
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']

            # Authenticating User
            user = auth.authenticate(username=username, password=password)

            # Validating User
            if user is not None:
                auth.login(request, user)
                messages.info(request, 'Welcome!')
                return redirect('/')

            # If invalid user
            else:
                messages.info(request, 'Invailid Username or Password')
                return redirect('/login') 
    
        else:
            return render(request, 'login.html')
    # If user is already login        
    else:
        messages.info(request, 'Already Login')
        return redirect('/')                   

# Registartion of new User
def register(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            # Checking if user already registered
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Already Registered')
                return redirect('/signup')

            else:
                # Resgistering new user    
                user = User.objects.create_user(username = email, password = password, email = email, first_name = name)
                user.save()
                print('User added')
                messages.info(request, 'Account Created Successfully')
                return redirect('/login')

        else:
            return render(request, 'register.html')
    
    # if user is already logined        
    else:
        return redirect('/')          

# Logout User
def logout(request):
    auth.logout(request)
    messages.info(request, 'Thank You, Come Again')
    return redirect('/login')

@login_required(login_url='/login') #Decorator to check authentication if not then redirect to login page
def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        dob = request.POST['date']

        # Creating new employee
        newEmployee = Empolyee(emp_name=name, emp_email=email, emp_contact=contact, emp_gender=gender, emp_dob=dob)
        newEmployee.save()

        # showing message of success
        messages.info(request,'Employee Added')
        return redirect('/')

    else:
        return render(request, 'create.html')

# Updating employee data 
@login_required(login_url='/login')
def update(request, id):
    # Filter desired user using id
    emp = Empolyee.objects.filter(emp_id=id)
    myDate = emp[0].emp_dob
    # Changing data formate 
    formatedDate = myDate.strftime("%Y-%m-%d")

    # If request is post    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        dob = request.POST['date']
        
        # Updating user information
        emp.update(emp_name = name, emp_email = email, emp_contact = contact, emp_gender = gender, emp_dob = dob)
        
        messages.info(request,'Employee Data Updated')
        return redirect('/')

    else:
        param={'employees':emp, 'date':formatedDate}
        return render(request, 'update.html', param)


# Delete User
@login_required(login_url='/login')
def delete(request, id):
    # Get targeted employee
    emp = Empolyee.objects.filter(emp_id=id)
    # Delete employee data
    emp.delete()
    messages.info(request, 'Employee Record Deleted')
    return redirect('/')