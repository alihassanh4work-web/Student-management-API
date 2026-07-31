from django.urls import path
from .views import *

urlpatterns = [
    path('students/', student_list),
    path('add-student/', add_student),
    path('update-student/<int:id>/', update_student),
    path('delete-student/<int:id>/', delete_student),

]