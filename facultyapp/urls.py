from django.urls import path, include
from .import views
app_name='facultyapp'
urlpatterns=[
    path('FacultyHomePage', views.FacultyHomePage, name='FacultyHomePage'),
    path('add_course', views.add_course, name='add_course'),
    path('view_student_list', views.view_student_list, name='view_student_list'),
    path('post_marks', views.view_student_list, name='post_marks'),
    path('feedback/', views.submit_feedback, name='feedback'),
    path('feedback/list/', views.feedback_list, name='feedback_list'),
    path('qq', views.qq, name='post_marks'),

]