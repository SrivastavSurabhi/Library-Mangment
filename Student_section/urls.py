from django.contrib import admin
from django.urls import path,include
from Student_section import views

urlpatterns = [
    path('RegisterStudent',views.Register,name="Registration"),
    path('ViewMember',views.MemberRecords, name="viewmember"),
    path('delete/<int:Member_IdNumber>',views.deleteInfo,name="delete"),
    path('update/<int:Member_IdNumber>',views.update_data,name="update"),

    path('searchmember', views.Search_Member, name="searchmember"),

    path('memberlogin', views.Memberlogin, name="memberlogin"),

]