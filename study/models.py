from django.db import models

class Student(models.Model):
    """
    Models for student
    """
    full_name = models.CharField(max_length=144)


    def __str__(self):
        return f"{self.full_name}"


class Teacher(models.Model):
    """
    Models for teacher 
    """
    full_name =models.CharField(max_length=144)


    def __str__(self):
        return f"{self.full_name}"

class Course(models.Model):
    """
    Models for course
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}"

class Lesson(models.Model):
    """
    Models for lesson
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
