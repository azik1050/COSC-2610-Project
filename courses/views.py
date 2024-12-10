from django.shortcuts import render
from django.views.generic import ListView
from courses.models import Course, Student, Timetable


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/courses_page.html'
    queryset = Course.objects.order_by('-updated_at')


class StudentsListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'courses/students_page.html'
    queryset = Student.objects.order_by('-start_date')



def timetable_view(request):
    level = request.GET.get('level')
    timetable_levels = Timetable.LEVELS

    if level:
        timetables = Timetable.objects.filter(student_level=level)
    else:
        timetables = Timetable.objects.all()

    data = {
        'timetable_levels': timetable_levels,
        'schedules': timetables
    }
    return render(request, 'courses/schedules_page.html', data)
