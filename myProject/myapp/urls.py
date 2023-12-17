from django.urls import path
from .views import index, student_detail, home, about, calculate, result, Result, student_create, student_update, student_list, student_delete, teacher_detail, course_detail

urlpatterns = [
    path('', index, name="index"),
    path('home', home, name="home"),
    path('about', about, name="about"),
    path('calculate', calculate, name="calculate"),
    path('result', Result.as_view(), name="result"),

    # Student Links
    path('students', student_list, name='student_list'),
    path('students/<int:pk>', student_detail, name='student_detail'),
    path('students/create', student_create, name='student_create'),
    path('students/<int:pk>/update', student_update, name='student_update'),
    path('students/<int:pk>/delete', student_delete, name='student_delete'),

    # Course Links
    path('teacher/<int:teacher_id>',teacher_detail, name='teacher_detail'),
    path('course/<int:course_id>',course_detail, name='course_detail')

    # path('student/<int:pk>', student_detail, name="detail")
]