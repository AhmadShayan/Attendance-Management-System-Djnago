from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_list, name='attendance_list'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('remove-attendance/<int:attendance_id>/', views.remove_attendance, name='remove_attendance'),
]
