from django.urls import path, include
from . import views

#/home - default homepage after login, displays courses,profs reviewed
#/member/username - shows user details and decent activity
#/index - Has search, displays most popular courses, profs
#/course/course_id - displays all reviews of the course, profs with best 
#/Prof/prof_id - Professor reviews, with courses taken by the Prof
#/invalid - When an invalid login is encountered
#/register
#/login
#/logout
#/settings - Change password, convert reviews to anonymous
#/profile/id - View user's profile
urlpatterns = [
    path('', views.home),
    path('login/', views.log_in, name='login'),
    path('check/', views.check, name='check'),
    path('home/', views.home, name='home'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.reg, name='register'),
    path('check_r/', views.check_r, name='check_r'),
    path('courses/', views.courses, name='courses'),
    path('professors/', views.professors, name='profs'),
    path('course/view/<str:code>', views.course_view,name='course_view'),
    path('prof/view/<int:ID>', views.prof_view, name='prof_view'),
    path('course_review_submit/', views.course_review_submit, name='course_review_submit'),
    path('prof_review_submit/', views.prof_review_submit, name='prof_review_submit'),
    path('profile/<int:ID>/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('course/view/<str:CODE>/Reviews/<str:sort>/<int:page>',views.CourseReviewList, name='course_review_list'),
    path('prof/view/<int:CODE>/Reviews/<str:sort>/<int:page>', views.ProfReviewList, name='prof_review_list'),
    path('myreviews/course/<int:page>', views.UserCourseReviewList, name='user_course_review_list'),
    path('myreviews/prof/<int:page>', views.UserProfReviewList, name='user_prof_review_list'),
    path('settings/', views.settings, name='settings'),
    path('settings/changepassword', views.changePassword, name='changepassword'),
    path('settings/passwordChanger', views.passwordChanger, name='passwordChanger'),
]