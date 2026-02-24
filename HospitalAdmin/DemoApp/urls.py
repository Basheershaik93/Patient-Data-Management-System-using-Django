from django.urls import path
from DemoApp import views
from django.contrib.auth import views as g


urlpatterns =[
    path('',views.home,name="hm"),
    path('Admin_login/',g.LoginView.as_view(template_name="html/Admin_login.html"),name="ad"),
    path('Medical_login/',views.Medical_login,name="me"),
    path('Insurance_login/',views.Insurnace_login,name="in"),
    path('Hospital_Department/',views.Hospital,name='ho'),
    path('Medical_Department/',views.Medical_Dept,name='med'),
    path('Insurance_Department/',views.Insurance_Dept,name='ins'),
    path('patient_details/',views.patient_details,name='patient_details'),
    path('view_medical_bill/<str:patient_id>/', views.view_medical_bill, name='view_medical_bill')
]
