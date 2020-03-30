from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import loader
from django.core.paginator import Paginator
from .models import Courses, Professors, Professor_Reviews, Course_Reviews, BannedList, CourseRatingList,CourseUpvoteList,ProfRatingList,ProfUpvoteList
import datetime
#TO DO:
# Implement rating,upvote feature
# change password page
# Putting all links
# Improve design
def BanCheck(name):
    try:
         q = BannedList.objects.get(Student__username = name)
    except BannedList.DoesNotExist:
        return False
    endT = q.EndDate
    diff = endT - datetime.datetime.now()
    if diff.total_seconds() > 0:
        return True
    else:
        return False    

def check(request):
    if request.user.is_authenticated:
        return redirect('/Reviews/home')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            if BanCheck(username):
                return redirect('/Reviews/home')
            
            else:
                login(request, user)
                return redirect('/Reviews/home')
        else:
            return redirect('/Reviews/login')

def log_in(request):
    if request.user.is_authenticated:
        return redirect('/Reviews/home')
    else:
        request.session['login'] = False
        global initialize
        initialize = True
        return render(request, 'Reviews/login.html')
def home(request):
    if request.user.is_authenticated:
        q = Professor_Reviews.objects.filter(Student__username = request.user.username).order_by('-Date')[:3]
        r = Course_Reviews.objects.filter(Student__username = request.user.username).order_by('-Date')[:3]
        return render(request, 'Reviews/home.html', {'q':q, 'r':r})
    else:
        return render(request, 'Reviews/home.html')
def log_out(request):
    #request.session['login'] == False
    #del request.session['username']
    logout(request)
    return redirect('/Reviews/login')
def reg(request):
    if request.user.is_authenticated:
        return redirect('/Reviews/home')
    else:
        return render(request, 'Reviews/registration.html')
def check_r(request):
    def is_email(string):
        from django.core.exceptions import ValidationError
        from django.core.validators import EmailValidator
        validator = EmailValidator()
        try:
            validator(string)
        except ValidationError:
            return False
        return True 
    def IITDEmailCheck(mail):
        if ("iitd.ac.in") in mail:
            a = User.objects.filter(username__contains = (mail.split(".")[0]))
            if a.exists():
                return False
            else:
                return True
        else:
            return False
    username = request.POST.get('username')
    email = request.POST.get('email')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')
    if is_email(email) and password==confirm and IITDEmailCheck(email):
        user = User.objects.create_user(username,email,password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/Reviews/home')
        else:
            return redirect('/Reviews/register')
    else:
        return redirect('/Reviews/register')

def courses(request):
    course_list = Courses.objects.order_by('-Ratings')[:10]
    context = {'course_list': course_list}
    return render(request, 'Reviews/courses.html', context)

def professors(request):
    prof_list = Professors.objects.order_by('-Ratings')[:10]
    context = {'prof_list': prof_list}
    return render(request, 'Reviews/professors.html', context)

def course_view(request, code):
    try:
        q = Courses.objects.get(Course_Code = code)
    except Courses.DoesNotExist:
        raise Http404("Course doesn't exist")
    r = Course_Reviews.objects.filter(Course__Course_Code = code).order_by('-Upvotes')[:10]
    s = Course_Reviews.objects.filter(Course__Course_Code = code).order_by('-Date')[:10]
    t = Course_Reviews.objects.filter(Course__Course_Code = code).filter(Student__username = request.user.username)
    if t.count()!=0:
        Reviewed = True
    else:
        Reviewed = False
    return render(request, 'Reviews/course_view.html', {'q':q,'r':r,'s':s,'t':t,'Reviewed':Reviewed})

def prof_view(request, ID):
    try:
        q = Professors.objects.get(id = ID)
    except Professors.DoesNotExist:
        raise Http404("Professor data not found")
    r = Professor_Reviews.objects.filter(Professor__id = ID).order_by('-Upvotes')[:10]
    s = Professor_Reviews.objects.filter(Professor__id = ID).order_by('-Date')[:10]
    t = Professor_Reviews.objects.filter(Professor__id = ID).filter(Student__username = request.user.username)
    if t.count()!=0:
        Reviewed = True
    else:
        Reviewed = False
    return render(request, 'Reviews/prof_view.html', {'q':q, 'r':r, 's':s,'t':t, 'Reviewed':Reviewed})

def course_review_submit(request):
    if request.user.is_authenticated:
        text = request.POST.get('Review')
        #anon = request.POST.get('anon')
        CODE = request.POST.get('CODE')
        if request.POST.get('anon') == "1":
            anon = True
        else:
            anon = False
        q = Course_Reviews(Student = request.user, Review = text, Anonymous = anon, Upvotes = 0, Course = Courses.objects.get(Course_Code = CODE))
        q.save()
        return redirect('/Reviews/course/view/%s' %CODE)
    else:
        return redirect('/Reviews/login')

def prof_review_submit(request):
    if request.user.is_authenticated:
        text = request.POST.get('Review')
        ID = request.POST.get('ID')
        if request.POST.get('anon') == "1":
            anon = True
        else:
            anon = False
        q = Professor_Reviews(Student = request.user, Review = text, Anonymous = anon, Upvotes = 0, Professor = Professors.objects.get(id = ID))
        q.save()
        return redirect('/Reviews/prof/view/%s' %ID)
    else:
        return redirect('/Reviews/login')

def profile(request, ID):
    try:
        q = User.objects.get(id = ID)
    except User.DoesNotExist:
        raise Http404("User not found")
    r = Course_Reviews.objects.filter(Student__id = ID).order_by('-Date')[:3]
    s = Professor_Reviews.objects.filter(Student__id = ID).order_by('-Date')[:3]
    return render(request, 'Reviews/profile.html',{'q':q, 'r':r, 's':s})

def search(request):
    text = request.POST.get('search')
    q = Courses.objects.filter(Course_Code__contains = text)
    r = Professors.objects.filter(Name__contains = text)
    return render(request, 'Reviews/search.html',{'q':q, 'r':r})

def CourseReviewList(request, sort, page, CODE):
    if sort =='Date' or sort == 'Upvotes':
        query_sort = "-" + sort
        q = Course_Reviews.objects.filter(Course__Course_Code = CODE).order_by(query_sort)
        paginator = Paginator(q, 3)
        page_obj = paginator.get_page(page)
        return render(request, 'Reviews/course_review_view.html',{'page_obj':page_obj, 'sort':sort, 'CODE':CODE})

def ProfReviewList(request, sort, page, CODE):
    if sort =='Date' or sort == 'Upvotes':
        query_sort = "-" + sort
        q = Professor_Reviews.objects.filter(Professor__id = CODE).order_by(query_sort)
        paginator = Paginator(q, 3)
        page_obj = paginator.get_page(page)
        return render(request, 'Reviews/prof_review_view.html',{'page_obj':page_obj, 'sort':sort, 'CODE':CODE})

def UserProfReviewList(request, page):
    if request.user.is_authenticated:
        q = Professor_Reviews.objects.filter(Student__username = request.user.username).order_by('-Date')
        paginator = Paginator(q, 5)
        page_obj = paginator.get_page(page)
        return render(request, 'Reviews/user_prof_review_view.html',{'page_obj':page_obj})
    else:
        return redirect('/Reviews/home')

def UserCourseReviewList(request, page):
    if request.user.is_authenticated:
        q = Course_Reviews.objects.filter(Student__username = request.user.username).order_by('-Date')
        paginator = Paginator(q, 5)
        page_obj = paginator.get_page(page)
        return render(request, 'Reviews/user_course_review_view.html', {'page_obj':page_obj})
    else:
        return redirect('/Reviews/home')

def settings(request):
    if request.user.is_authenticated:
        return render(request, 'Reviews/settings.html')
    else:
        return redirect('/Reviews/login')
def changePassword(request):
    if request.user.is_authenticated:
        return render(request, 'Reviews/change_password.html')
    else:
        return redirect('/Reviews/login')
def passwordChanger(request):
    if request.POST.get('password') == request.user.password and request.POST.get('new')==request.POST.get('confirm'):
        u = User.objects.get(username = request.user.username)
        u.set_password(request.POST.get('new'))
        u.save()
        return redirect('/Reviews/home')
    else:
        return redirect('/Reviews/settings')