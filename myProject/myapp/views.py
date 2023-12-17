from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import Student, Teacher, Course, Candidate
from .forms import StudentForm

# Create your views here.

def teacher_detail(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    courses = teacher.courses.all()
    context = {
        'teacher' : teacher,
        'courses' : courses
    }

    return render(request, 'teacher_detail.html', context)

def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    students = course.students.all()
    context = {
        'students' : students,
        'course' : course
    }

    return render(request, 'course_detail.html', context)

'''
C - Create
R - Read
U - Update
D - Delete
'''

def student_list(request):
    students = Student.objects.all()
    context = {
        'students' : students
    }
    return render(request, 'list.html', context)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student' : student
    }
    return render(request, 'detail.html', context)

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        
    else:
        form = StudentForm()
        return render(request, 'create.html', { 'form' : form })

def student_update(request,pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
        
    else:
        form = StudentForm(instance=student)
        context = {
            'form' : form,
            'student' : student
        }
        return render(request, 'update.html', context)
    

'''
def student_create(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mothers_maiden_name = request.POST['mothers_maiden_name']
        biography = request.POST['biography']
        age = request.POST['age']

        Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            age = age,
            biography = biography,
            mothers_maiden_name = mothers_maiden_name
        )

        return redirect('student_list')
    
    return render(request, 'create.html')

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.mothers_maiden_name = request.POST['mothers_maiden_name']
        student.biography = request.POST['biography']
        student.age = request.POST['age']

        student.save()

        return redirect('student_detail', pk = pk)

    return render(request, 'update.html', { 'student' : student})
    
'''

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    
    return render(request, 'delete.html', { 'student' : student})


class Result(View):
    def get(self, request):
        return HttpResponse("You are seeing this because it is not a post request")
    
    def post(self, request):
        firstNumber = request.POST['num1']
        secondNumber = request.POST['num2']
        op = request.POST['operator']
        op_match = {
            "plus":"+",
            "minus":"-",
            "times":"*",
            "divide": "/"
        }
        expression = f"{firstNumber}{op_match[op]}{secondNumber}"
        result = eval(expression)

        context = {
            "result": result
        }

        return render(request, "result.html", context)

def index(request):
    return render(request, "index.html")

def home(request):
    context = {
        'user' : 'Alexander',
        'total_points' : 2700
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def calculate(request):
    return render(request, "calculator.html")

def result(request):

    if request.method == "POST":

        firstNumber = request.POST['num1']
        secondNumber = request.POST['num2']
        op = request.POST['operator']
        op_match = {
            "plus":"+",
            "minus":"-",
            "times":"*",
            "divide": "/"
        }
        expression = f"{firstNumber}{op_match[op]}{secondNumber}"
        result = eval(expression)

        context = {
            "result": result
        }

        return render(request, "result.html", context)
        

# def student_detail(request, pk):
#     return HttpResponse(f"This is the detail page of the user with the id of {pk}")