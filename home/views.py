from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from .models import info, facultyt, securityt, role, visitort, appointments
import uuid
from .forms import appointmentForm, facultyForm, visitorForm, securityForm, loginForm
# Create your views here.
def home(request):
    return render(request,'index.html')


def login(request):
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            try:
                query = role.objects.get(username = u )
                if(query.roles == 'security'):
                    try:
                        obj = securityt.objects.get(username = u, password = p)
                        return redirect(security,username=u)

                    except securityt.DoesNotExist:
                        messages.error(request, "Username and Password donot match")
                elif(query.roles == 'faculty'):
                    try:
                        obj = facultyt.objects.get(username = u, password = p)
                        return redirect(faculty, username=u)

                    except facultyt.DoesNotExist:
                        messages.error(request, "Username and Password donot match")
                elif(query.roles == 'visitor'):
                    try:
                        obj = visitort.objects.get(username = u, password = p)
                        return redirect(visitor, username=u)
                    except visitort.DoesNotExist:
                        messages.error(request, "Username and Password donot match")
            except role.DoesNotExist:
                messages.error(request, "Username and Password donot match")
               
        else:
            form = facultyForm()
    return render(request,'login.html',{'form':form})



def register(request):
    form1 = facultyForm()
    form2 = securityForm()
    form3 = visitorForm()
    if request.method == 'POST' and 'submit1' in request.POST:
        form1 = facultyForm(request.POST)
        if form1.is_valid():
            try:
                query = role.objects.get(username=form1.cleaned_data['username'])
                messages.error(request, "Username or Email Address already taken")
            except:    
                query = role(username = form1.cleaned_data['username'], roles = 'faculty')
                form1.save()
                query.save()
                return redirect("home")
        else:
            form1 = facultyForm()
            messages.error(request, "Username or Email Address already taken")
    elif request.method == 'POST' and 'submit2' in request.POST:
        form2 = securityForm(request.POST)
        if form2.is_valid():
            try:
                query = role.objects.get(username=form2.cleaned_data['username'])
                messages.error(request, "Username or Email Address already taken")
            except:    
                query = role(username = form2.cleaned_data['username'], roles = 'faculty')
                form2.save()
                query.save()
                return redirect("home")
        else:
            form2 = securityForm()
            messages.error(request, "Username or Email Address already taken")        
    elif request.method == 'POST' and 'submit3' in request.POST:
        form3 = visitorForm(request.POST,request.FILES)
        print(form3.is_valid())
        print(form3.errors)
        if form3.is_valid():
            try:
                query = role.objects.get(username=form3.cleaned_data['username'])
                messages.error(request, "Username or Email Address already taken")
            except:    
                query = role(username = form3.cleaned_data['username'], roles = 'visitor')
                form3.save()
                query.save()
                return redirect("home")
        else:
            form3 = visitorForm()
            messages.error(request, "Username or Email Address already taken")        
    context = {'form1':form1, 'form2':form2, 'form3':form3}
    return render(request,'register.html',context)   



def security(request,username):
    text = "<h1>Security<h1>"
    return HttpResponse(text)
def faculty(request,username):
    text = "<h1>faculty<h1>"
    return HttpResponse(text)
def visitormail(request,username,fid):
    form = appointmentForm()
    if request.method == "POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            query = info.objects.get(id=fid)
            d = form.cleaned_data['doa']
            t = form.cleaned_data['timeIn']
            p = form.cleaned_data['purpose']
            obj=appointments(username = username, 
            email = query.email, 
            doa = d,
            timeIn = t,
            purpose = p)
            obj.save()
            emailfaculty(obj.id)
            # messages.error(request, "Emailed faculty check your appointments for status") 
            return redirect(visitor,username=username)
        else:
            form = appointmentForm()
    context = {'form':form,'uname':username, 'ffid': fid}
    return render(request,"visitormail.html",context)
def visitor(request,username):
    obj = info.objects.all()
    context = {'obj':obj}
    return render(request,'visitor.html',context)

def emailfaculty(oid):
    obj = appointments.objects.get(id=oid)
    print(obj)
    tok = str(uuid.uuid4())
    obj.token = tok
    obj.save()
    message = f'Hi {obj.username} {obj.timeIn} {obj.doa} {obj.purpose} http://127.0.0.1:8000/accept/{tok} or http://127.0.0.1:8000/decline/{tok} '
    send_mail('SUBJECT',
    message,
    'aakashgusain2806@gmail.com',
    [str(obj.email)],
    fail_silently=False)
    print(obj.email)
    text = "<h1>random<h1>"
def accept(request,tokenid):
    obj = appointments.objects.get(token=tokenid)
    obj.status = "Accepted"
    obj.save()
    return HttpResponse("accept")
def decline(request,tokenid):
    obj = appointments.objects.get(token=tokenid)
    obj.status = "Declined"
    obj.save()
    return HttpResponse("decline")
