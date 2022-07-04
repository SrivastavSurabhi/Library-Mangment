from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.views.generic.edit import UpdateView

from .models import Book_Record,IssueBook_Record
from Student_section.models import Student_table
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    return render(request,'Home.html')

def CreateUser(request):
    if request.method == "POST":
        usernm = request.POST.get('user-username')
        password = request.POST.get('user-password')
        email = request.POST.get('user-email')
        firstnm = request.POST.get('user-firstname')
        lastnm = request.POST.get('user-lastname')
        user = User.objects.create_user(usernm,email,password)
        user.first_name = firstnm
        user.last_name = lastnm
        user.save()
        messages.success(request, "Create User successfully ! Now you can Access as Staff User.....")

    return render(request,'Home.html')


def Userlogin(request):
        if request.method == "POST":
            usernm = request.POST.get('username')
            passwd = request.POST.get('password')
            # check if user has entered correct credentials
            user = authenticate(username=usernm,password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request,"User successfully Logged In ! Now you can Access Current Application ......")
                return redirect('/')
            else:
                messages.error(request, 'User login failed ! Please Enter correct credentials')
                return redirect('/')

        return render(request, 'Home.html')

def Userlogout(request):
        logout(request)
        messages.success(request, "User successfully Logged Out ! Please Re_Login for Access again .....")
        return redirect('/')

def addBook(request):
    if request.method == 'POST':
        bookid = request.POST.get('book-id')
        booktitle = request.POST.get('book-title')
        author = request.POST.get('book-author')
        catergory = request.POST.get('catergory')
        quantity= request.POST.get('quantity')
        details= Book_Record(Book_Id=bookid,Book_Title=booktitle,Author_Name=author,Catergory=catergory,Quantity=quantity)
        details.save()
        messages.success(request, 'Book Added Successfully !')


    return render(request,"Add_Book.html")

def viewBook(request):
    stud = Book_Record.objects.all()
    messages.info(request, 'you can Delete/Update Particularly Record in Existing Book Records ......!')
    return render(request, 'View_Books.html', {'stu': stud} )

def issueBook(request):
    if request.method == 'POST':
        memberid = request.POST.get('member-id')
        membername = request.POST.get('member-name')
        bookid = request.POST.get('book-id')
        booktitle= request.POST.get('book-title')
        issuedate= request.POST.get('issue-date')
        lastdate= request.POST.get('last-date')
        record = IssueBook_Record(Member_IdNumber=memberid,Member_Name=membername,Book_Id=bookid,
                                  Book_Title=booktitle,Issuedate=issuedate,Expirydate=lastdate)
        memberCheck = Student_table.objects.filter(Member_IdNumber__exact=memberid, Member_Name__exact=membername)
        bookCheck = Book_Record.objects.filter(Book_Id__exact=bookid, Book_Title__exact=booktitle)
        if not memberCheck:
            messages.error(request, 'Member Not Verified ! Enter correct credentials /Register as New Member')
        elif not bookCheck:
            messages.error(request, 'Book Not Existing In Records ! Please Enter Existing Book credentials')
        else:
            record.save()
            messages.success(request, 'Issue Book Successfully ! ')

    return render(request,'Issue_Book.html')

def viewIssue(request):
    reco = IssueBook_Record.objects.all()
    return render(request, 'Issued_Records.html', {'stu': reco} )

def delete_bookInfo(request,Book_Id):
    if request.method=='POST':
        delt = Book_Record.objects.get(pk=Book_Id)
        delt.delete()
        messages.error(request, 'Book Record Successfully Deleted ! ')
        return HttpResponseRedirect('/viewbook')

class Update(UpdateView):
    stud =Book_Record.objects.all()
    model = Book_Record #model
    fields = ['Book_Id','Book_Title','Author_Name','Catergory','Quantity'] # fields / if you want to select all fields, use "__all__"
    template_name = 'Update_data.html'# templete for updating
    success_url="/viewbook"



def delete_issueInfo(request,id):
    if request.method=='POST':
        delt = IssueBook_Record.objects.get(pk=id)
        delt.delete()
        messages.error(request, 'Issued Book Successfully Returned ! ')
        return HttpResponseRedirect('/viewissue')

def Search_book(request):
    query = request.GET['searchbook']
    allPosts =Book_Record.objects.filter(Book_Title__contains = query)#this command is for search.
    #allPosts =InsertBook.objects.all()

    return render(request,'View_Books.html',{'stu': allPosts})

def Search_issue(request):
    query = request.GET['searchrecord']
    allPosts =IssueBook_Record.objects.filter(Member_Name__contains = query)#this command is for search.
    #allPosts =InsertBook.objects.all()

    return render(request, 'Issued_Records.html', {'stu': allPosts})




