from django.shortcuts import render
from .models import User
from .models import Security_db
from .models import Faculty_db
from .models import Details_db
from .models import Appointments_db
import mysql.connector
from django.contrib import messages
from operator import itemgetter
from django.contrib  import auth 
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.http import HttpResponse
import uuid

# Create your views here.

def welcome(req):
	return render(req,'welcome.html')
def login(req):
	con = mysql.connector.connect(host="localhost",user="root",passwd="Airtel1234",database="hello")
	cursor=con.cursor()
	con2 = mysql.connector.connect(host="localhost",user="root",passwd="Airtel1234",database="hello")
	cursor2=con2.cursor()
	sqlcommand="select uname from log_user"
	sqlcommand2="select password from log_user"
	cursor.execute(sqlcommand)
	cursor2.execute(sqlcommand2)
	e=[]
	p=[]
	for i in cursor:
		e.append(i)
	for j in cursor2:
		p.append(j)
	res=list(map(itemgetter(0),e))
	res2=list(map(itemgetter(0),p))	
	con3 = mysql.connector.connect(host="localhost",user="root",passwd="Airtel1234",database="hello")
	cursor3=con3.cursor()
	con4 = mysql.connector.connect(host="localhost",user="root",passwd="Airtel1234",database="hello")
	cursor4=con4.cursor()
	sqlcommand3="select uname from log_faculty_db"
	sqlcommand4="select password from log_faculty_db"
	cursor3.execute(sqlcommand3)
	cursor4.execute(sqlcommand4)
	e1=[]
	p1=[]
	for i in cursor3:
		e1.append(i)
	for j in cursor4:
		p1.append(j)
	res3=list(map(itemgetter(0),e1))
	res4=list(map(itemgetter(0),p1))
	con5 = mysql.connector.connect(host="localhost",user="root",passwd="Airtel1234",database="hello")
	cursor5=con5.cursor()
	con6 = mysql.connector.connect(host="localhost",user="root",passwd="Airtel1234",database="hello")
	cursor6=con6.cursor()
	sqlcommand5="select uname from log_security_db"
	sqlcommand6="select password from log_security_db"
	cursor5.execute(sqlcommand5)
	cursor6.execute(sqlcommand6)
	e2=[]
	p2=[]
	for i in cursor5:
		e2.append(i)
	for j in cursor6:
		p2.append(j)
	res5=list(map(itemgetter(0),e2))
	res6=list(map(itemgetter(0),p2))
	if req.method=="POST":
		uname = req.POST['uname']
		password = req.POST['password']
		i = 1
		k = len(res)
		while i<k:
			if res[i]==uname and res2[i]==password:
				return render(req,'visitorpage.html')
				break
			i=i+1

		i = 1
		k = len(res3)
		while i<k:
			if res3[i]==uname and res4[i]==password:
				return render(req,'facultypage.html')
				break
			i=i+1

		i = 1
		k = len(res5)
		while i<k:
			if res5[i]==uname and res6[i]==password:
				return render(req,'securitypage.html')
				break
			i=i+1

	else:
		return render(req,'login.html')
	return render(req,'login.html')
def signin(req):
	return render(req,'signin.html')
def visitorsignin(req):
	if req.method=="POST":
		user= User()

		user.fname=req.POST['fname'].upper()
		user.lname=req.POST['lname'].upper()
		user.email=req.POST['email']
		user.uname=req.POST['uname']
		user.password=req.POST['password']
		user.gender=req.POST['gender'].upper()
		user.date_field=req.POST['date_field']

		user.save()
		
	return render(req,'visitorsignin.html')
def facultysignin(req):
	if req.method=="POST":
		faculty_db = Faculty_db()

		faculty_dbfname=req.POST['fname'].upper()
		faculty_db.lname=req.POST['lname'].upper()
		faculty_db.email=req.POST['email']
		faculty_db.uname=req.POST['uname']
		faculty_db.password=req.POST['password']
		faculty_db.save()
	return render(req,'facultysignin.html')
def securitysignin(req):
	if req.method=="POST":
		security_db= Security_db()

		security_db.fname=req.POST['fname'].upper()
		security_db.lname=req.POST['lname'].upper()
		security_db.email=req.POST['email']
		security_db.uname=req.POST['uname']
		security_db.password=req.POST['password']
		security_db.gender=req.POST['gender'].upper()
		security_db.date_field=req.POST['date_field']

		security_db.save()
	return render(req,'securitysignin.html')

def securitypage(req):
	return render(req,'securitypage.html')

def secview(req):
	allapp = Appointments_db.objects.all()
	print("I AM AN ASSHOLE")
	print(allapp)
	return render(req,'secview.html',{'p':allapp})


def visitorpage(req):
	return render(req,'visitorpage.html')

def facultypage(req):
	return render(req,'facultypage.html')

def makeapp(req):
	alldata = Details_db.objects.all()

	if req.method=="POST":
		appointments_db= Appointments_db()

		appointments_db.fname=req.POST['fname'].upper()
		appointments_db.lname=req.POST['lname'].upper()
		appointments_db.fullname_of_visitor=req.POST['fullname_of_visitor']
		appointments_db.purpose=req.POST['purpose']
		appointments_db.date_ofapp= req.POST['date_ofapp']

		appointments_db.save()
	
	return render(req,'makeapp.html',{'d':alldata})
	
def viewappvisitor(req):
	return render(req,'viewappvisitor.html')




def random(request,fid):
    print(fid)
    obj = Details_db.objects.get(id=fid)
    token = str(uuid.uuid4())
    obj.auth = token
    obj.save()
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/login/{token}'
    send_mail('SUBJECT',
    message,
    'b18cs030@nitm.ac.in',
    [str(obj.email)],
    fail_silently=False)
    print(obj.email)
    text = "<h1>Message Sent<h1>"
    
    return HttpResponse(text)
