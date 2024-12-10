from django.contrib import admin
from .models import Course, Student, Timetable


class StudentTabularInline(admin.TabularInline):
    model = Student
    extra = 0

    fields = ("firstname", "lastname", "slug", "seniority")
    prepopulated_fields = {"slug": ("firstname",)}

    show_change_link = True
    show_full_result_count = True


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'students')
    list_display_links = ('name',)
    list_filter = ('updated_at',)

    fields = (('name', 'slug'),)
    prepopulated_fields = {'slug': ('name',)}

    search_fields = ('name',)
    search_help_text = 'Enter name of course'

    list_per_page = 50
    save_as = True

    inlines = [StudentTabularInline]

    def students(self, obj):
        if obj:
            students_count = Student.objects.filter(course=obj).count()
            return students_count
        else:
            return 0


class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'middlename', 'lastname', 'course', 'gender', 'seniority', 'start_date')
    list_filter = ('seniority', 'start_date', 'course', 'gender')
    list_editable = ('seniority',)
    list_display_links = ('firstname',)

    search_fields = ('firstname', 'middlename', 'lastname')
    search_help_text = 'Enter name of student'

    list_per_page = 50
    save_as = True

    fieldsets = [
        ('Main info', {
            'fields': [
                ('firstname', 'lastname'),
                'middlename', 'slug',
                'date_of_birth', 'gender'
            ],
        }),
        (
            'Additional info', {
                'fields': [
                    'seniority', 'course',
                    ('start_date',)
                ]
            }
        )
    ]
    prepopulated_fields = {'slug': ('firstname',)}


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('course', 'room', 'student_level', 'day', 'time', 'students')
    list_display_links = ('course',)
    list_editable = ('day', 'time', 'room', 'student_level')

    fields = ('course', 'student_level', 'room', ('day', 'time'))

    list_per_page = 50

    search_fields = ('course__name',)
    search_help_text = 'Enter name of course'

    def students(self, obj):
        if obj.course:
            students_count = Student.objects.filter(course=obj.course).count()
            if students_count:
                return students_count
            return 0


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Timetable, TimetableAdmin)
