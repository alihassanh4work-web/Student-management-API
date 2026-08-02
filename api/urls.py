from django.urls import path
from .views import *

urlpatterns = [
    path('students/', student_list),
    path('add-student/', add_student),
    path('update-student/<int:id>/', update_student),
    path('delete-student/<int:id>/', delete_student),
    path('courses/', course_list),
    path('add-course/', add_course),
    path('update-course/<int:id>/', update_course),
    path('delete-course/<int:id>/', delete_course),
    path('teacher/', teacher_list),
    path('add-teacher/', add_teacher),
    path('update-teacher/<int:id>/', update_teacher),
    path('delete-teacher/<int:id>/', delete_teacher),
    path('classrooms/', classroom_list),
    path('add-classroom/', add_classroom),
    path('update-classroom/<int:id>/', update_classroom),
    path('delete-classroom/<int:id>/', delete_classroom),
]