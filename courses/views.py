from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')


def view_students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
