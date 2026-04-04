from django.shortcuts import render,redirect

from .models import Employee1
from .models import Employee



def crud(request):
    res = Employee.objects.all()
    return render(request, 'crud.html',{'edata': res})


def delrec(req,Eid):
    res=Employee.objects.get(Eid=Eid)
    res.delete()
    return redirect(crud)

def uprec(req,Eid):
    res=Employee.objects.get(Eid=Eid)
    return render(req, 'update.html',{'empdata':res})
def update(req):
    if req.method=="POST":
        a = req.POST.get('eid')
        b = req.POST.get('ename')
        c = req.POST.get('phno')
        d = req.POST.get('sal')
        res = Employee.objects.get(Eid=a)
        res.Ename = b
        res.Phno = c
        res.Salary = d
        res.save()
        return redirect(crud)
    else:
        return render(req,'update.html')

def insert(req):
    if req.method=="POST":
        a=req.POST.get('eid')
        b=req.POST.get('ename')
        c=req.POST.get('Phno')
        d=req.POST.get('sal')
        res=Employee(Eid=a,Ename=b,Phno=c,Salary=d)
        res.save()
        return redirect(crud)
    else:
        return render(req,'insert.html')
from django.shortcuts import render

# Create your views here.
