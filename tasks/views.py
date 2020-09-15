from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from .models import User_db
from django.core.paginator import Paginator

# Create your views here.


# -------------------------------------- Static pages -----------------------------------------



                                # Home page
def home(request):
    return render(request,'home.html')





                                # Success page
def success(request):
    return render(request,'success.html')





                                # Login page
def login(request):
    return render(request,'login.html')





                                # Registration page
def registration(request):
    return render(request,'registration.html')







# -------------------------------------- Outer Forms --------------------------------------------



                                # Registration Form Submit
def reg_form(request):

    if(request.method=="POST"):
        name = request.POST['name']
        mobile = request.POST['phone']
        role = request.POST['role']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['confrim_password']

        if(password==password_confirmation):
            user = User_db.objects.filter(email=email).count()
            if(user):
                messages.info(request,"Email id already exists !")
                return render(request,'registration.html')

            else:
                password = make_password(password)
                user=User_db(name=name,mobile=mobile,email=email,password=password,role=role,address=address)
                user.save()
                return redirect('/success')
                
            

        else:
            messages.info(request,"Password not same !")
            return render(request,'registration.html')

    else:
        messages.info(request,"Method is not POST !")
        return render(request,'registration.html')    



    






                                # Login Form Submit
def login_form(request):

    if(request.method=="POST"):
        email = request.POST['email']
        user = User_db.objects.filter(email=email).count()
        if(user):
            user =  User_db.objects.get(email=email)
            password = request.POST['password']

            if(check_password(password,user.password)):
                request.session['user']=user.id
                request.session['role']=user.role
                request.session['name']=user.name
                request.session['photo']=user.photo.url
                
                return redirect('/admin-dashboard')
                

            else:
                
                messages.info(request,"Invalid user id or password !")
                return render(request,'login.html')

        else:
            
            messages.info(request,"Invalid user id or password !")
            return render(request,'login.html')

    







# -------------------------------------- Admin pages --------------------------------------------


                                # Admin dashboard page
def admin_dashboard(request):

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).count()
        if(user):
            total = User_db.objects.all().count()
            return render(request,'admin-dashboard.html',{'total_users':total})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')








                                # Logout
def logout(request):
    request.session.clear()
    return redirect('/login')









                                # Admin Add user page
def admin_add_user(request):
    return render(request,'admin-add-user.html')








                                # Admin All users page
def admin_all_users(request):
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).count()
        if(user):
            users = User_db.objects.all()
            return render(request,'admin-all-users.html',{'users':users})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')




                                # Admin profile update page
def admin_profile_update(request):
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).count()
        if(user):
            user =  User_db.objects.get(id=request.session['user'])
            
            return render(request,'admin-profile-update.html',{'name':user.name,'mobile':user.mobile,'email':user.email,'address':user.address,'photo':user.photo.url})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')









                                # Admin USER profile update page
def admin_update_user(request):
    return render(request,'admin-update-user.html')



# -------------------------------------- Admin tasks --------------------------------------------


def admin_profile_update_form(request):
    
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).count()
        if(user and request.method=="POST"):
            user =  User_db.objects.get(id=request.session['user'])
            
            user.name=request.POST["name"]
            user.mobile=request.POST["mobile"]
            user.address=request.POST["address"]

            if(request.POST['password']!=""):
                user.password = make_password(request.POST['password'])
            user.save()
            return redirect("/admin-profile-update")
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')








def admin_profile_photo_update(request):

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).count()
        if(user and request.method=="POST"):
            user =  User_db.objects.get(id=request.session['user'])
            photo = request.FILES["photo"]
            user.photo = photo
            user.save()
            return redirect("/admin-profile-update")
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
            







def ajax_call_delete_user(request):
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).count()
        if(user and request.method=="POST"):
            user = User_db.objects.filter(id=request.POST['id']).count()
            if(user):
                id = request.POST['id']
                User_db.objects.filter(id=id).delete()
                return JsonResponse({"value":id},status=200)
            else:
                return JsonResponse({"value":0})
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})










def profile_edit_by_get(request,id):

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).count()
        if(user):
            user =  User_db.objects.get(id=id)
            
            return render(request,'admin-update-user.html',{'id':id,'name':user.name,'mobile':user.mobile,'email':user.email,'address':user.address,'role':user.role,'photo':user.photo.url})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')










def user_profile_update_form(request):
    
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).count()
        inp_user = User_db.objects.filter(id=request.POST['id']).count()

        if(user and inp_user and request.method=="POST"):
            user =  User_db.objects.get(id=request.POST['id'])
            
            user.name=request.POST["name"]
            user.mobile=request.POST["mobile"]
            user.address=request.POST["address"]
            user.role=request.POST["role"]

            if(request.POST['password']!=""):
                user.password = make_password(request.POST['password'])
            user.save()
            return redirect("/admin-all-users")
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')








def user_profile_photo_update(request):         

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).count()
        inp_user = User_db.objects.filter(id=request.POST['id']).count()
        if(user and inp_user and request.method=="POST"):
            user =  User_db.objects.get(id=request.POST['id'])
            photo = request.FILES["photo"]
            user.photo = photo
            user.save()
            return redirect("/admin-all-users")
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')















def admin_new_user_profile_form(request):
    
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).count()

        user2 = User_db.objects.filter(email=request.POST["email"]).count()
        if(user2):
            messages.info(request,"Email id already exists !")
            return redirect('/admin-add-user')

        if(user and request.method=="POST"):
            user =  User_db()
            
            user.email=request.POST["email"]
            user.name=request.POST["name"]
            user.mobile=request.POST["mobile"]
            user.address=request.POST["address"]
            user.role=request.POST["role"]
            user.password = make_password(request.POST['password'])

            
            if(request.FILES):
                user.photo = request.FILES["photo"]

            user.save()

            return redirect("/admin-all-users")
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

