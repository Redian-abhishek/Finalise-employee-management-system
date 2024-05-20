from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp
from django.db.models import Count

from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import logout

from django.db.models import Q

from django.contrib.auth.decorators import login_required
def emp_home(request):
    if request.user.is_authenticated:
        emps = Emp.objects.all()
        return render(request, "emp/home.html", {'emps':emps})
    # 
    else:
        # Redirect to the sign-in page if the user is not authenticated
        return redirect('emp/signin')

def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    print("Yes Bhai")
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
    return redirect("/emp/home/")


def signup(request):
 
    if request.user.is_authenticated:
        return redirect('emp/home/')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('/emp/home')
         
        else:
            return render(request,'signup.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})


def signout(request):
    logout(request)
    return redirect('signin') 


def signin(request):
    if request.user.is_authenticated:
        return redirect('/emp/home/')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/emp/home')
        else:
            form = AuthenticationForm()
            return render(request,'signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})
    

def search(request):
    query = request.GET.get('q')
    employees = Emp.objects.all()

    if query:
        employees = employees.filter(                        
            Q(id__icontains=query) |
            Q(emp_id__icontains=query) |
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(address__icontains=query)|
            Q(department__icontains=query)
        )
    return render(request, "search.html", {'emps': employees, 'query': query})

def chart(request):
    # Query the database to retrieve the data
    employees = Emp.objects.all()

    # Process the data to count the number of employees for each working status
    working_count = employees.filter(working=True).count()
    not_working_count = employees.filter(working=False).count()

    # Process the data to count the number of employees in each department
    department_counts = employees.values('department').annotate(count=Count('department'))

    departments = [d['department'] for d in department_counts]
    department_counts = [d['count'] for d in department_counts]

    # Pass the data to the template
    context = {
        'working_count': working_count,
        'not_working_count': not_working_count,
        'departments': departments,
        'department_counts': department_counts,
    }
    
    return render(request, 'chart.html', context)