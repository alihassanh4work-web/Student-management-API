from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True) # Convert multiple Student objects into JSON data
    return Response(serializer.data)

@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def update_student(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({"message": "Student deleted successfully"})

@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True) # Convert multiple Course objects into JSON data
    return Response(serializer.data)

@api_view(['POST'])
def add_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def update_course(request, id):
    course = Course.objects.get(id=id)
    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return Response({"message": "Course deleted successfully"})

@api_view(['GET'])
def teacher_list(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True) # Convert multiple Teacher objects into JSON data
    return Response(serializer.data)

@api_view(['POST'])
def add_teacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def update_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    serializer = TeacherSerializer(teacher, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return Response({"message": "Teacher deleted successfully"})

@api_view(['GET'])
def classroom_list(request):
    classrooms = Classroom.objects.all()
    serializer = ClassroomSerializer(classrooms, many=True) # Convert multiple Classroom objects into JSON data
    return Response(serializer.data)

@api_view(['POST'])
def add_classroom(request):
    serializer = ClassroomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def update_classroom(request, id):
    classroom = Classroom.objects.get(id=id)
    serializer = ClassroomSerializer(classroom, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_classroom(request, id):
    classroom = Classroom.objects.get(id=id)
    classroom.delete()
    return Response({"message": "Classroom deleted successfully"})