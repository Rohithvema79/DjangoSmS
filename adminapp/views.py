import calendar
import datetime
import string
import random

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm
from .models import Task


# Create your views here.
def htmlpage(request):
    return render(request,'adminapp/index.html')

def printpagecall(request):
    return render(request,'adminapp/printer.html')

def printpagelogic(request):
    if request.method=="POST":
        user_input = request.POST['user_input']
        print(f'user input: {user_input}')
    a1={'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)
def exceptionpagecall(request):
    return render(request, 'adminapp/print_to_console.html')
from django.shortcuts import render



def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')
        try:
            result = process_user_input(user_input)
            return render(request, 'adminapp/print_to_console.html', {'result': result})
        except Exception as e:
            return render(request, 'adminapp/print_to_console.html', {'error': str(e)})
    return render(request, 'adminapp/print_to_console.html')
def process_user_input(user_input):
    try:
        num = int(user_input)
        result = 10 / num
        return result
    except ZeroDivisionError:
        raise Exception('Cannot divide by zero.')
    except ValueError:
        raise Exception('Invalid input. Please enter a valid number.')

def exceptionpagecall(request):
        return render(request, 'adminapp/printer2.html')

def exceptionpagelogic(request):
        if request.method == "POST":
            user_input = request.POST['user_input']
            result = None
            error_message = None
            try:
                num = int(user_input)
                result = 10 / num
            except Exception as e:
                error_message = str(e)
            return render(request, 'adminapp/printer2.html', {'result': result, 'error': error_message})
        return render(request, 'adminapp/printer2.html')


def randompagecall(request):
    return render(request, 'adminapp/Randomexample.html')

def randomlogic(request):
    if request.method=="POST":
        number1=int(request.POST['number1'])
        ran=''.join (random.sample(string.ascii_uppercase+string.digits,k=number1 ))
    a1={'ran':ran}
    return render(request,'adminapp/Randomexample.html',a1)

def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2

        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})


def calculatorpagecall(request):
    return render(request, 'adminapp/calculator.html')


def datetimepagecall(request):
    return render(request,'adminapp/datetime1.html')

def datetimepagelogic(request):
    if request.method=="POST":
        number1=int(request.POST['date1'])
        x=datetime.datetime.now()
        ran= x + datetime.timedelta(days=number1)
        ran1=ran.year
        ran2=calendar.isleap(ran1)
        if ran2==False:
            ran3="NOT A LEAP YEAR"
        else:
            ran3="Leap year"
        a1={'ran':ran,'ran3':ran3,'ran1':ran1,'number1':number1}
        return render(request, 'adminapp/datetime1.html',a1)


def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form=TaskForm()
    tasks= Task.objects.all()
    return render(request,'adminapp/add_task.html',{'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/Register.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/Register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/Register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/index.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/Register.html')
    else:
        return render(request, 'adminapp/Register.html')
def UserLoginPageCall(request):
    return render(request, 'adminapp/Login.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/login.html')
    else:
        return render(request, 'adminapp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('htmlpage1')

from .forms import StudentForm
from .models import StudentList

# def add_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm()
#     return render(request, 'adminapp/add_student.html', {'form': form})


from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})

def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})