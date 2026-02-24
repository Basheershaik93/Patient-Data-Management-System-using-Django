from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login
from .models import Patient,Invoice
import json,os
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request,'html/start.html')

def Admin(request):
    return render(request, 'html/admin_login.html')

def Medical_login(request):
    if request.method=="POST":
        n=request.POST['Name']
        pa=request.POST['password']
        if(n=="Medical93" and pa=="Medical@93"):
            return redirect('med')

    return render(request,'html/Medical_login.html')

def Insurnace_login(request):
    if request.method=="POST":
        n=request.POST['username']
        pa=request.POST['password']
        if(n=="Insurance93" and pa=="Insurance@93"):
            return redirect('ins')
    return render(request,'html/Insurance_login.html')



def Hospital(request):
    k=Patient.objects.count()
    b=k+1
    t=Patient.objects.all()
    if request.method=="POST":
        p=request.POST['Patient']
        n=request.POST['Name']
        a=request.POST['Age']
        g=request.POST['gender']
        e=request.POST['Email']
        ad=request.POST['address']
        d=request.POST['description']
        t=request.POST['PaymentType']        
        x=Patient.objects.create(PatientId=p,name=n,age=a,Gender=g,Email=e,Address=ad,Description=d,PaymentType=t)
        b+=1
        request.session["pati"]=b
        return redirect('ho')
    return render(request,'html/Hospital.html',{'l':b,'f':t})

def Medical_Dept(request):
    patients = Patient.objects.all()
    
    l = " has Created Successfully in real Time \u2705"  

    #b="Medical bill generated successfully \u2705"
    
    if request.method == "POST":
        p = request.POST.get('na')
        if p:  
            x = Patient.objects.get(PatientId=p)
            k = x.name
            d = x.Description
            q = x.Email
            f = x.PatientId
            
            t = Medicine_details()
            t_json = json.dumps(t)
            
            return render(request, 'html/Medical.html', {'patients': patients, 'z': l, 'id': f, 'w': k, 'e': d, 'Q': q, 'q': t, 'q_json': t_json})
        
        v = request.POST.get('MedicineT')
        if v:
            print(v)
            medicine_name = v
            quantity = 1  
            total_amount = request.POST.get('totalAmount')
            pato=request.POST.get('patan')
            print(pato)

            invoice = Invoice.objects.create( patient=pato,medicine_name=medicine_name, quantity=quantity, total_amount=total_amount)
            invoice.save()

    return render(request, 'html/Medical.html', {'patients': patients})


def Insurance_Dept(request):
    t=Patient.objects.all()
    i=Invoice.objects.all()
    try:
        if request.method == "POST":
            p = request.POST.get('na')
            x = Patient.objects.get(PatientId=p)
            e=x.PaymentType
            if(e=="Insurance"):
                a=x.name
                k=x.Email
                f = x.PatientId
                x.Acceptance="Accepted"
                x.save()
                return render(request,'html/Insurance.html',{'X':f,'I':i,'A':a,'K':k,'id':f})
    except:
        y="Patient Id didn't Match.Please Enter correct Patient Id \u274C"
        return render(request,'html/Insurance.html',{'Y':y})
    return render(request,'html/Insurance.html',{'f':t})

def patient_details(request):
    patients = Patient.objects.all()  
    return render(request, 'html/patient_details.html', {'patients': patients})

def Medicine_details():
    l={'Paracetamol':50,'Ibuprofen':80,'Aspirin':65,'Acetaminophen':55,'Naproxen':70,'Antihistamines':60,'Decongestants':70,'Cough Syrup':120,'Throat Lozenges':40,'Cold Tablets':90,
       'Acetaminophen':55,'Ibuprofen':80,'Aspirin':65,'Naproxen':70,'Sumatriptan':150,}
    return l



def view_medical_bill(request, patient_id):
    k=patient_id
    patient = Patient.objects.get(PatientId=patient_id)
    
    invoices = Invoice.objects.all()
    
    return render(request, 'html/view_medical_bill.html', {'z':k,'patient': patient, 'invoices': invoices})