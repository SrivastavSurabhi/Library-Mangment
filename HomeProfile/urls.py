from django.contrib import admin
from django.urls import path
from .import views
from .views import Update

urlpatterns = [
    path('',views.home,name="home"),
    path('createuser',views.CreateUser,name="createuser"),

    path('userlogin',views.Userlogin,name="userlogin"),
    path('userlogout',views.Userlogout,name="userlogout"),

    path('addbook',views.addBook,name="addbook"),
    path('viewbook',views.viewBook,name="viewbook"),
    path('issuebook',views.issueBook,name="issuebook"),
    path('viewissue',views.viewIssue,name="viewissue"),
    path('deletebook/<int:Book_Id>', views.delete_bookInfo, name="deletebook"),
    path('updatebook/<slug:pk>', Update.as_view(), name="updatebookdata"),

    path('deleteissue/<int:id>', views.delete_issueInfo, name="deleteissuebook"),
    path('searchbook/', views.Search_book , name="search"),
    path('searchrecord/', views.Search_issue , name="searchrecord"),


]
