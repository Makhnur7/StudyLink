from django.urls import path

from . import views

urlpatterns = [
    path('students/', view=views.StudentListCreateAPIView.as_view()),
    path('teacher/', view=views.TeacherListCreateView.as_view()),
    path('lesson/', view=views.LessonListCreateView.as_view()),
    path('courses/', view=views.CourseListCreateView.as_view()),
    path('courses/<int:pk>/', view=views.CourseRetrieveUpdateDestroyView.as_view()),
    path('lesson/<int:pk>/', view=views.LessonRetrieveUpdateDestroyView.as_view()),
]