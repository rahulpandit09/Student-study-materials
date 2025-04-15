from django.contrib import admin
from django.urls import path
from study import views


urlpatterns = [
        path('contact/', views.contact, name='contact'),

    path('', views.notes, name="notes"),
    # all course
    path('bca/', views.bca),
    path('bsc/', views.bsc),
    path('bcom/', views.bcom),
    path('bba/', views.bba),

    # masters Computers Science and commerse science
    path('master-cs/', views.master),
    path('commers-mc/', views.commers),

    # all Semseter BBA
    path('semester1/', views.semseter1),
    path('semester2/', views.semseter2),
    path('semester3/', views.semseter3),
    path('semester4/', views.semseter4),
    path('semester5/', views.semseter5),
    path('semester6/', views.semseter6),

    # all Semester BCA
    path('sem1/',views.sem1),
    path('sem2/',views.sem2),
    path('sem3/',views.sem3),
    path('sem4/',views.sem4),
    path('sem5/',views.sem5),
    path('sem6/',views.sem6),

   # all Semester Bsc
    path('text1/',views.text1),
    path('text2/',views.text2),
    path('text3/',views.text3),
    path('text4/',views.text4),
    path('text5/',views.text5),
    path('text6/',views.text6),

# all Semester Bcom
    path('semesters1/',views.semesters1),
    path('semesters2/',views.semesters2),
    path('semesters3/',views.semesters3),
    path('semesters4/',views.semesters4),
    path('semesters5/',views.semesters5),
    path('semesters6/',views.semesters6),


    
]
