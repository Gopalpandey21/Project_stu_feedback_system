from django.shortcuts import render, redirect
from datetime import datetime
from Form import settings
from activity.models import Student, Faculty, Feedback
from django.contrib import messages
from django.contrib.auth import  logout
from django.core.files.storage import default_storage
import os
# Create your views here.

def index(request):
    return render(request, 'form.html')

def about(request):
    return render(request, "about.html")


def registration(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        mobile = request.POST.get('mobile')
        program = request.POST.get('program')
        semester = request.POST.get('semester')
        dob = request.POST.get('dob')
        profilePic = request.FILES.get('profilePic')

        # Check if password matches confirm password
        if password == confirmpassword:
            # Check if email is already registered
            if Student.objects.filter(email=email).exists():
                messages.success(request, "You are already registered!")
                return render(request, "studlogin.html")
            else:
                # Check if profile picture is uploaded
                if profilePic:
                    # Create the directory to store profile pictures if it doesn't exist
                    profile_pic_dir = os.path.join(settings.MEDIA_ROOT, 'profile_pics')
                    if not os.path.exists(profile_pic_dir):
                        os.makedirs(profile_pic_dir)

                    # Save the image to the media directory
                    profile_pic_path = default_storage.save(os.path.join('profile_pics', profilePic.name), profilePic)

                    # Create the student entry
                    entry = Student.objects.create(
                        username=name, email=email, password=password, confirmPassword=confirmpassword,
                        mobile=mobile, program=program, semester=semester, dob=dob, profilePic=profile_pic_path,
                        loginDate=datetime.today()
                    )
                    messages.success(request, "You have been registered!")
                    return render(request, "studlogin.html")
                else:
                    messages.error(request, "Please upload a profile picture")
        else:
            messages.error(request, "Password not matched!")

    return render(request, "Registration.html")



def studlogin(request):
    if(request.method == "POST"):
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:  
            request.session['email'] = email
            request.session['password'] = password
            
            obj = Student.objects.get(email=email,password=password)
            img = (str(obj.profilePic))
            request.session['username'] = obj.username
            request.session["mobile"] = obj.mobile
            request.session['dob'] = str(obj.dob)
            request.session['img'] = img
            context = {
                'username':obj.username,
                'email':email,
               'src': "/media/" + img
            }
            return render(request,'studentdashboard.html',context)
        except:
            messages.warning(request, "You have not yet registered !")
            return redirect("register")
    return render(request,'studlogin.html')

def updatepassword(request):
    email = request.session['email']
    orgpass = request.session['password']
    username = request.session['username']
    img = str(Student.objects.get(email=email).profilePic)
    context = {
        "message" : 'Values don\'t match',
        'username':username,
        'email':email,
       'src': "/media/" + img
    }
    if(request.method=='POST'):
        oldpass =  request.POST.get('oldPassword')
        newpass =  request.POST.get('newPassword')
        conpass =  request.POST.get('confirmPassword')
        if(orgpass==oldpass):
            if(newpass==conpass):
                Student.objects.all().filter(email=email).update(password=newpass)
                messages.success = 'Your Password Changed Successfully'
                print(email)

        return render(request,'studentdashboard.html',context)
    return render(request,'updatepassword.html' ,context)
   
def updateinfo(request):
    email = request.session['email']
    username = request.session['username']
    dob = request.session['dob']
    mobile = request.session['mobile']
    img = str(Student.objects.get(email=email).profilePic)
    print(username)
    context = {
        "message" : 'Values does not match',
        'username':username,
        'email':email,
        'src': "/media/" + img
    }
    if(request.method=='POST'):
        name =  request.POST.get('name')
        semail =  request.POST.get('email')
        fmobile =  request.POST.get('mobile')
        fdob =  datetime.strptime(request.POST.get('dob'),"%Y-%m-%d")
        print(fdob,type(fdob))
        if(email==semail):
                Student.objects.all().filter(email=semail).update(username=name,email=semail,dob=fdob,mobile=fmobile)
                messages.success = 'Your Information Changed Successfully'
                print(email)

        return render(request,'studentdashboard.html',context)
    return render(request,'updateprofile.html' ,context)



def stufeedback(request):
    email = request.session['email']
    username = request.session['username']
    
    facu = Faculty.objects.all()
    
    img = str(Student.objects.get(email=email).profilePic)
    context = {
        "message": 'Values does not match',
        'username': username,
        'email': email,
        'faculties': facu,
        'src': "/media/" + img
    }

    # if request.method == 'POST':
    #     facuname = request.POST.get('facu')
    #     q1 = request.POST.get('radioGroupq1')
    #     q2 = request.POST.get('radioGroupq2')
    #     q3 = request.POST.get('radioGroupq3')
    #     q4 = request.POST.get('radioGroup2q1')
    #     q5 = request.POST.get('radioGroup2q2')
    #     q6 = request.POST.get('radioGroup2q3')
    #     q7 = request.POST.get('radioGroup3q1')
    #     q8 = request.POST.get('radioGroup3q2')
        
    #     avg = int(q1) + int(q2) + int(q3) + int(q4) + int(q5) + int(q6) + int(q7) + int(q8)
    #     rating = avg / 8

    #     # Set rating and message in session
    #     request.session['rating'] = rating
    #     if rating >= 5:
    #         request.session['message'] = 'Excellent'
    #     elif rating >= 3:
    #         request.session['message'] = 'Good'
    #     else:
    #         request.session['message'] = 'Normal'

    #     entry = Feedback(name=facuname, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, rating=rating)
    #     entry.save()

    # return render(request, "feedback.html", context)

    if request.method == 'POST':
     facuname = request.POST.get('facu')
    q1 = request.POST.get('radioGroupq1')
    q2 = request.POST.get('radioGroupq2')
    q3 = request.POST.get('radioGroupq3')
    q4 = request.POST.get('radioGroup2q1')
    q5 = request.POST.get('radioGroup2q2')
    q6 = request.POST.get('radioGroup2q3')
    q7 = request.POST.get('radioGroup3q1')
    q8 = request.POST.get('radioGroup3q2')
    
    # Check if any of the values are None or empty
    if not all([q1, q2, q3, q4, q5, q6, q7, q8]):
          messages.warning(request, "You have not empty any value")
    else:
        avg = int(q1) + int(q2) + int(q3) + int(q4) + int(q5) + int(q6) + int(q7) + int(q8)
        rating = avg / 8
        

        # Set rating and message in session
        request.session['rating'] = rating
        if rating >= 5:
            request.session['message'] = 'Excellent'
        elif rating >= 3:
            request.session['message'] = 'Good'
        else:
            request.session['message'] = 'Normal'

        entry = Feedback(name=facuname, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, rating=rating)
        entry.save()

    return render(request, "feedback.html", context)



def logout_view(request):
    logout(request)
    return redirect('index')



def facufeedback(request):
    feeddata = Feedback.objects.all()
    email = request.session['email']
    name = request.session['name']
    fimg = str(Faculty.objects.get(email=email).pic)
    context = {
        "message" : 'Values don\'t match',
        'name':name,
        'email':email,
        'feeddata':feeddata,
        'src': "/media/" +fimg
    }
    return render(request,'facultyfeedback.html',context)


def flogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        request.session['email'] = email
        request.session['password'] = password
        try:
            fobj = Faculty.objects.get(email=email, password=password)
            fimg = str(fobj.pic)
            request.session['name'] = fobj.name
            request.session['designation'] = fobj.designation
            request.session['programme'] = fobj.programme
            request.session['mobile'] = fobj.mobile
            request.session['fimg'] = fimg
            context = {
                'name': fobj.name,
                'email': email,
                'src': "/media/" + fimg
            }
            
            # Pass rating and message to faculty dashboard template if available
            if 'rating' in request.session:
                context['rating'] = request.session['rating']
                context['message'] = request.session['message']
                # del request.session['rating']  # Remove rating from session
                # del request.session['message']  # Remove message from session
            
            return render(request, 'facultydashboard.html', context)
        except Faculty.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('facultylogin')
    return render(request, 'facultylogin.html')





def facupdatepass(request):
    email = request.session['email']
    facorgpass = request.session['password']
    name = request.session['name']
    fimg = str(Faculty.objects.get(email=email).pic)
    context = {
        "message" : 'Values don\'t match',
        'name':name,
        'email':email,
        'src': "/media/" +fimg
    }
    
    if(request.method=='POST'):
        oldpass =  request.POST.get('oldPassword')
        newpass =  request.POST.get('newPassword')
        conpass =  request.POST.get('confirmPassword')
        if(facorgpass==oldpass):
            if(newpass==conpass):
                Faculty.objects.all().filter(email=email).update(password=newpass)
                context['message'] = 'Password Changed Successfully'

        return render(request,'facupdatepass.html',context)
    return render(request,'facupdatepass.html' ,context)

def facupdateinfo(request):
    email = request.session['email']
    name = request.session['name']
    mobile = request.session['mobile']
    fimg = str(Faculty.objects.get(email=email).pic)
    context = {
        "message" : 'Values don\'t match',
        'name':name,
        'email':email,
        'src': "/media/" +fimg
    }
    if(request.method=='POST'):
        name =  request.POST.get('name')
        femail =  request.POST.get('email')
        fmobile =  request.POST.get('mobile')
        fdesignation =  request.POST.get('designation')
        fprogram = request.POST.get('program')
        if(email==femail):
                Faculty.objects.all().filter(email=femail).update(name=name,email=femail,mobile=fmobile,designation=fdesignation,program=fprogram)
                context['message'] = 'Information Changed Successfully'
                print(email)

        return render(request,'facupdateinfo.html',context)
    return render(request,'facupdateinfo.html' ,context)



def alogin(request):
    return render(request,'admindashboard.html')