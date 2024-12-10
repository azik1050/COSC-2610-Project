from django.urls import path
from . import views


urlpatterns = [
    path('', views.CourseListView.as_view(), name='course-list'),
    path('students/', views.StudentsListView.as_view(), name='student-list'),
    path('schedules/', views.timetable_view, name='schedule-list'),
]

