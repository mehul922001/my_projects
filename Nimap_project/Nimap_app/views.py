from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from datetime import datetime
import pytz
from .forms import LoginForm,RegisterForm,ClientForm,ProjectForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import ClientModel,projectUserModel,ProjectModel
from django.contrib.auth import get_user_model


# Create your views here.

class home(View):
    
    def get(self,request):
        # print(datetime.now(pytz.timezone('asia/calcutta')))
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:

            form = LoginForm()

            return render(request,'Nimap_temp/home.html',{'form':form})
        # return HttpResponse(status=204)
    
    def post(self,request):
        

        form = LoginForm(request.POST,data=request.POST)
        if form.is_valid():
            print('form is valid')
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            print(u_name)
            print(u_pass)
            user = authenticate(username = u_name,password = u_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged In Succesfully !!!')
                return redirect('dashboard')
            print('wrong email or pass')
            messages.warning(request,'Wrong Email Id or Password !!!')
            return redirect('home')



class register(View):
    
    def get(self,request):
        
        form = RegisterForm()

        return render(request,'Nimap_temp/register.html',{'form':form})


    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form)
            messages.success(request,'Registered Succesfully !!!')
            return redirect ('home')
        
        
        # messages.warning(request,'Something Went Wrong !!!')
        return render(request,'Nimap_temp/register.html',{'form':form})


class log_out(View):

    def get(self,request):
        logout(request)
        form = LoginForm()
        messages.success(request,'Logged Out Succesfully !!!')
        return redirect('home')
    
    def post(self,request):
        pass


class all_clients(View):

    def get(self,request):

        data = ClientModel.objects.all()
        print(data)
        print('data is above')
        return render(request,'Nimap_temp/all_clients.html',{'data':data})
    
    def post(self,request):
        pass

class add_client(View):

    def get(self,request):
        form = ClientForm()
        return render(request,'Nimap_temp/add_client.html',{'form':form})     
    
    def post(self,request):
        form = ClientForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['client_name']
            print(form['client_name'])
            form.save()
            data = ClientModel.objects.get(client_name = client_name)
            print(data.id)
            # print(datetime.now(pytz.timezone('asia/calcutta')))
            data.created_at = datetime.now(pytz.timezone('asia/calcutta'))
            user = request.user
            data.created_by = str(user)
            data.save()
            print('data is printed above')
            messages.success(request,'Client Added Succesfully !!!')
            return redirect('all_clients')

        form = ClientForm()
        messages.warning(request,"Unable To Add... Client Name Either Already Exists or is invalid.....!!!")
       
        return render(request,'Nimap_temp/add_client.html',{'form':form})
        # print(client_name)
        


class update_client(View):

    def get(self,request,pk):
        data = ClientModel.objects.get(id=pk)
        return render(request,'Nimap_temp/update_client.html',{'data':data})
    
    def post(self,request,pk):
        
        data = ClientModel.objects.all()
        Present = False
        c_name = request.POST['client_name']
        c_name = c_name.strip()
        print(f"{len(c_name)} {len(request.POST['client_name'])}")
        print(c_name)
        for d in data:
            if d.client_name == c_name:
                Present = True
                break
        if Present == True:
            messages.warning(request,"Unable To Update... Client Name Either Already Exists or is invalid.....!!!")
            return redirect('all_clients')
        else:
            data = ClientModel.objects.get(id=pk)
            # print(request.POST['client_name'])
            # print('data is above')
            data.client_name = request.POST['client_name']
            data.updated_by = str(request.user)
            data.updated_at = datetime.now(pytz.timezone('asia/calcutta'))
            data.save()
            messages.success(request,'Client Updated Succesfully...!!!')
            return redirect('all_clients')

class delete(View):

    def get(self,request,pk):

        data = ClientModel.objects.get(id=pk)
        data.delete()
        return redirect('all_clients')

    
    def post(self,request):
        pass


class client_details(View):

    def get(self,request,pk):

        data = ClientModel.objects.get(id=pk)
        client_name = data.client_name
        projects = ProjectModel.objects.filter(client_name = client_name)
        print(projects)
        return render(request,'Nimap_temp/client_details.html',{'data':data,'projects':projects})

    
    def post(self,request):
        pass


class add_project(View):

    def get(self,request,pk):
        id=pk
        print(id)
        form = ProjectForm()
        user = get_user_model()
        users = user.objects.all().exclude(is_superuser = True)
        print(users)
        return render(request,'Nimap_temp/add_project.html',{'form':form,'users':users,'id':id})

    
    def post(self,request,pk):
        form = ProjectForm(request.POST)
        if form.is_valid():
            # print(form)
            p_name = form.cleaned_data['p_name']
            print(p_name)
            users_list = request.POST.getlist('users_assign')
            users = ','.join(users_list)
            print(users)
            client = ClientModel.objects.get(id=pk)
            client_name = client.client_name
            print(client_name)
            created_at = datetime.now(pytz.timezone('asia/calcutta'))
            data = ProjectModel()
            data.p_name = p_name
            data.client_name = client_name
            data.p_created_at = created_at
            data.p_created_by = str(request.user)
            data.users_assign = users
            data.save()
            record = ProjectModel.objects.last()
            l_record_id = record.id
            print('last record id is : ',l_record_id)
            print('asigned users : ',record.users_assign)
            print('Type of data : ',type(record.users_assign))
            u_assign_list = (record.users_assign).split(',')
            print(u_assign_list,type(u_assign_list))
            names = []
            for i in u_assign_list:
                obj=get_user_model()
                users = obj.objects.get(id=int(i))
                names.append(users.first_name)
            print(names)
            names = ','.join(names)

            for u in users_list:
                user_project = projectUserModel()

                print('user list item :',u)
                user_project.user = u
                user_project.projects = p_name
                user_project.client_name = client_name
                user_project.record_id = l_record_id
                user_project.user_assign_names = names
                user_project.created_at = created_at
                user_project.created_by = str(request.user)
                user_project.save()

            messages.success(request,'Project Added Succesfully...!!!')
            return redirect('projects')

            
class projects(View):

    def get(self,request):
        data = ProjectModel.objects.all()
        return render(request,'Nimap_temp/projects.html',{'data':data})

    
    def post(self,request):
        pass


class dashboard(View):

    def get(self,request):
        user = str(request.user)
        print(user,type(user))
        data = projectUserModel.objects.filter(user = request.user.id)

        return render(request,'Nimap_temp/dashboard.html',{'data':data,'user':user})
    
    def post(self,request):
        pass
