from django.shortcuts import render, redirect
from django import forms
from .models import Attendance, Student

class StudentForm(forms.Form):
    new_student = forms.CharField(label='New Student', max_length=100)

def mark_attendance(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        if student_id == 'manual':
            new_student_name = request.POST.get('new_student')
            student = Student.objects.create(name=new_student_name)
        else:
            student = Student.objects.get(pk=student_id)
        Attendance.objects.create(student=student)
        return redirect('attendance_list')
    else:
        students = Student.objects.all()
        new_student_form = StudentForm()
        return render(request, 'attendance/mark_attendance.html', {'students': students, 'new_student_form': new_student_form})
