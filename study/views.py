from rest_framework import generics

from .models import Student, Teacher, Course, Lesson
from .serializers import StudentSerializer, TeacherSerializer, LessonSerializer, CourseSerializer


class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class TeacherListCreateView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class CourseListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    
class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class LessonListCreateView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()