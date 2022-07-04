from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.http.response import HttpResponse
from django.contrib import messages

from .forms  import StudentForm
from .models import Student_table
from HomeProfile.models import IssueBook_Record




# Create your views here.

#Register New Records
def Register(request):
    if request.method == 'POST':
        stdform =StudentForm(request.POST)
        if stdform.is_valid():
            stdform.save()
            stdform = StudentForm()
            messages.success(request, 'Registered Member Successfully ! ')
    else:
        stdform = StudentForm()
        messages.success(request, 'Registered Member Successfully ! ')
    return render(request, 'Register_form.html',{'form':stdform})

def MemberRecords(request):
    stdInfo = Student_table.objects.all()
    return render(request, 'View_Members.html',{'Std':stdInfo } )


#Delete Records
def deleteInfo(request,Member_IdNumber):
    if request.method=='POST':
        delt = Student_table.objects.get(pk=Member_IdNumber)
        delt.delete()
        messages.error(request, 'Member Record Successfully Deleted ! ')
        return HttpResponseRedirect('/Student_section/ViewMember')

def update_data(request,Member_IdNumber):
    if request.method == 'POST':
        record = Student_table.objects.get(pk=Member_IdNumber)
        inst = StudentForm(request.POST, instance=record)
        if inst.is_valid():
            inst.save()
            messages.success(request, 'Registered Member Successfully Updated ! ')
    else:
        record = Student_table.objects.get(pk=Member_IdNumber)
        inst = StudentForm(instance=record)
    return render(request, 'Update_form.html', {'forms': inst})

def Search_Member(request):
    query = request.GET['searchmember']
    allPosts =Student_table.objects.filter(Member_Name__contains = query) #this command is for search.

    return render(request, 'View_Members.html', {'Std': allPosts})



def Memberlogin(request):
    if request.method == "POST":
        username = request.POST.get('member-username')
        password = request.POST.get('member-password')
        member =Student_table.objects.get(Set_Username__exact = username, Set_Password__exact = password )
        if member is not None:
            name=member.Member_Name
            record=IssueBook_Record.objects.filter(Member_Name__exact = name)
            return render(request,'Member_Profile.html', {'member':member,'record':record})

    return redirect('/')








