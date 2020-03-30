from django.contrib import admin
from .models import Courses, Professors, Course_Reviews, Professor_Reviews, BannedList, CourseUpvoteList, CourseRatingList, ProfRatingList,ProfUpvoteList
admin.site.register(Courses)
admin.site.register(Professors)
admin.site.register(Course_Reviews)
admin.site.register(Professor_Reviews)
admin.site.register(BannedList)
admin.site.register(CourseUpvoteList)
admin.site.register(CourseRatingList)
admin.site.register(ProfRatingList)
admin.site.register(ProfUpvoteList)
# Register your models here.
