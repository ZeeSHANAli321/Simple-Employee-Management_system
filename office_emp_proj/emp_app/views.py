from django.shortcuts import render,HttpResponse
from .models import Employee,Department,Role
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def addEmp(request):
    D=Department.objects.all()
    R=Role.objects.all()
    Context={
        'Ds':D,
        'Rs':R
    }
    if request.method=='POST':
        fn=request.POST.get('fname')
        ln=request.POST.get('lname')
        dept=int(request.POST.get('dept'))
        role=int(request.POST.get('role'))
        sal=request.POST.get('salary')
        bon=request.POST.get('bonus')
        ph=request.POST.get('phone')
        hd=request.POST.get('hdate')
        print(fn,ln,dept,role,sal,bon,ph,hd)
        Employee(f_name=fn,l_name=ln,dept=Department.objects.get(pk=dept),salary=sal,bonus=bon,phone=ph,hire_date=hd,role=Role.objects.get(pk=role)).save()
        return HttpResponse("<script>alert('Employee added Succesfully .. '); location.href='/addEmp';</script>")


    return render(request,'addEmp.html',Context)

def removeEmp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_remove=Employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("<script>alert('Employee Removed Succesfully .. '); location.href='/removeEmp';</script>")

        except: return HttpResponse("<script>alert('Enter valid Emp_id .. '); location.href='/removeEmp';</script>")
    emps = Employee.objects.all()
    Contaxt = {
        'emps':emps,
    }
    return render(request,'removeEmp.html',Contaxt)

def allEmp(request):
    emp = Employee.objects.all()
    Context = {
        'emps':emp
    }
    return render(request,'allEmp.html',Context)

def filterEmp(request):
    if request.method=="POST":
        n=request.POST.get('name')
        d=int(request.POST.get('dept'))
        r=int(request.POST.get('role'))
        print(n,d,r)
        emps = Employee.objects.all()

        if n:
            emps=emps.filter(Q(f_name__icontains = n) | Q(l_name__icontains = n))

        if d:
            if d!=0:
                emps=emps.filter(dept__id=d)
 
        if r:
            if r!=0:
                emps=emps.filter(role__id=r)
        Context={
            'emps':emps,
        }
        return render(request,'allEmp.html',Context)

    D=Department.objects.all()
    R=Role.objects.all()
    Context={
        'Ds':D,
        'Rs':R
    }
    return render(request,'filterEmp.html',Context)
