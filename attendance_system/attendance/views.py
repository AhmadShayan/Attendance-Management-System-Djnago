from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance, Student
from .forms import StudentForm

def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})


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
    
def remove_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    attendance.delete()
    return redirect('attendance_list')

