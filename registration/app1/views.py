from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from app1.models import Interest, StudentForm as StudentFormModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from app1.functions import handle_uploaded_file  #functions.py
from app1.forms import StudentForm #forms.py
from app1.retrieveInterestFromExcel import get_interest  # retrieveInterestFromExcel.py

user_email = ""  # for global variable https://stackoverflow.com/questions/12811523/django-global-variable
#profession = Mentee/Mentor
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    print("home",request.session.get('user_email'))
    get_interest = Interest.objects.filter(email=request.session.get('user_email'))
    
    
    my_interest = ""
    for interest in get_interest:
        my_interest= interest
   
    mylist = my_interest.interest.split(',')
    profession =my_interest.profession
    email = my_interest.email
    all_mentors_interests = Interest.objects.filter(profession='Mentor')
    mentor_list=[]
    for interest in mylist:
        for mentor in all_mentors_interests:
            skills = (mentor.interest.split(','))
            for skill in skills:
                if (skill.capitalize()) ==(interest.capitalize()):
                    mentor_list.append(mentor.email)
    
    unique_mentor_list = list(set(mentor_list))
    
    return render (request,'home.html',{'interestsList':mylist, 'mentorsList':unique_mentor_list, 'profession':profession,'email':email})

# for uploading excel, csv file of interests
def index(request):  
    if request.method == 'POST':  
        
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'],request.POST['email'])  
            model_instance = student.save(commit=False)
            model_instance.save()
            # Reading file path and email for that file -----------------
            get_files = StudentFormModel.objects.filter(email=request.POST['email'])
            for file in get_files:
                print(file.email, file.file.path)
                interest_string =  get_interest(file.file.path)  # reading interest written in that csv/xls file
                print(interest_string)
                Interest.objects.filter(email=request.POST['email']).update(interest=interest_string)
                # ---------------
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form':student}) 

# def mentor(request):
#     user_interest = Interest.objects.filter(email= user_email)
#     mentors_interest = Interest.objects.filter(profession=Mentor)
    

def SignupPage(request):
    if request.method=='POST':
        profession = request.POST.get('profession')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        interests = request.POST.get('interests')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            if User.objects.filter(username = uname).exists():
                return HttpResponse("Username already exists, Try Different!!")
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            user_interest = Interest(profession=profession,email=email,interest=interests)
            user_interest.save()
        #    -------------------Reading user email and Interest
            get_interests = (Interest.objects.all())
            for each_interest in get_interests:
                print(each_interest.profession,each_interest.email, each_interest.interest)
            #  --------------------------

            # return HttpResponse(Interest.objects.get(pk=1))
            return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            users  = User.objects.filter(username = username)
            email = ""
            for user in users:
                email = user.email
                user_email = email
                request.session['user_email'] = user_email
                print(request.session.get('user_email'))
                get_interest = Interest.objects.filter(email=email)
                for interes in get_interest:
                    print(email,interes.interest)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')