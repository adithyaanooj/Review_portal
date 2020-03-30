from django.db import models
from django.conf import settings

#Courses - Course Code(Primary key), Department, Name, Description, 
#Reviews - ID, Student(Foreign Key), Type(Prof/Course), Prof/Course ID(Foreign key), Upvotes, Anonymous, Published Date
#Professors - ID, Name, Department, 

class Courses(models.Model):
    Course_Code = models.CharField(primary_key = True,max_length = 6)
    Department = models.CharField(max_length = 50)
    Name = models.CharField(max_length = 100)
    Description = models.CharField(max_length = 250)
    Ratings = models.DecimalField(decimal_places = 3, max_digits = 3)
class Professors(models.Model):
    Name = models.CharField(max_length = 100)
    Department = models.CharField(max_length = 50)
    Ratings = models.DecimalField(decimal_places = 3, max_digits = 3)
class Professor_Reviews(models.Model):
    Student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    Professor = models.ForeignKey(Professors, on_delete = models.CASCADE)
    Upvotes = models.IntegerField()
    Anonymous = models.BooleanField()
    Date = models.DateTimeField(auto_now = True)
    Review = models.CharField(max_length = 2000)

class Course_Reviews(models.Model):
    Student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    Course = models.ForeignKey(Courses, on_delete = models.CASCADE)
    Upvotes = models.IntegerField()
    Anonymous = models.BooleanField()
    Date = models.DateTimeField(auto_now = True)
    Review = models.CharField(max_length = 2000)

class BannedList(models.Model):
    Student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    EndDate = models.DateTimeField()

class CourseUpvoteList(models.Model):
    Student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    Course = models.ForeignKey(Courses, on_delete = models.CASCADE)

class ProfUpvoteList(models.Model):
    Student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    Professor = models.ForeignKey(Professors, on_delete = models.CASCADE)
class ProfRatingList(models.Model):
    Student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    Professor = models.ForeignKey(Professors, on_delete = models.CASCADE)
class CourseRatingList(models.Model):
    Student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    Course = models.ForeignKey(Courses, on_delete = models.CASCADE)