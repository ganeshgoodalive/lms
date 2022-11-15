from django.shortcuts import render,redirect
#from library.forms import CourseForm
from library.models import Lib_Man_Sys_Table
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate
from library.forms import RegisterUser
# Create your views here.

#def registerformbased(request):
#    if request.method == 'POST':
#        uname = request.POST['username']
#        upass = request.POST['password2']
#        user =User(username=uname,password=upass,is_staff=1)
#        user.save()
#        return redirect('/registerformbased')
#        logout(request)
#    else:
#        f = UserCreationForm()
#        content = {'form':f}
#        logout(request)
#        return render (request,'register.html',content)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = RegisterUser(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password,is_staff=1)
                login(request, user)
                messages.success(request, 'Registration successfull')
                return redirect('/')
            else:
                messages.error(request, 'Registration failed')
                return redirect('register_user')
        else:
            form = RegisterUser()
            return render(request, 'register_user.html', {'form':form})



def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            usernam = request.POST['username']
            passwor = request.POST['password']
            user = authenticate(request, username=usernam, password=passwor)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/')

            else:
                messages.error(request, 'Wrong Credentials')
                return redirect('login')
        else:
            return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "logout successfull")
    return redirect('/login_user')

def home(request):
        datas=Lib_Man_Sys_Table.objects.filter(active='y')
        book_type = Lib_Man_Sys_Table.objects.values_list('book_type').distinct()
        data ={'datas':datas,'book_type' : book_type}
        return render(request,'home.html',context=data)


def data(request):
    if request.user.is_authenticated:
        data ={}
        data['datas']=Lib_Man_Sys_Table.objects.filter(active='y')
        data['book_type'] = Lib_Man_Sys_Table.objects.values_list('book_type').distinct()
        data['add_permission'] = request.user.has_perm('library.add_lib_man_sys_table')
        data['update_permission'] = request.user.has_perm('library.change_lib_man_sys_table')
        data['delete_permission'] = request.user.has_perm('library.delete_lib_man_sys_table')
        data['view_permission'] = request.user.has_perm('library.view_lib_man_sys_table')
        print(data['add_permission'],data['update_permission'])
        return render(request,'data.html',data)
    else:
        return render(request,'data.html')

def header(request):
    if request.user.is_authenticated:
        data ={}
        data['datas']=Lib_Man_Sys_Table.objects.filter(active='y')
        data['book_type'] = Lib_Man_Sys_Table.objects.values_list('book_type').distinct()
        data['add_permission'] = request.user.has_perm('library.add_lib_man_sys_table')
        data['update_permission'] = request.user.has_perm('library.change_lib_man_sys_table')
        data['delete_permission'] = request.user.has_perm('library.delete_lib_man_sys_table')
        data['view_permission'] = request.user.has_perm('library.view_lib_man_sys_table')
        print(data['add_permission'],data['update_permission'])
        return render(request,'library/header.html',data)
    else:
        return render(request,'library/header.html')

@login_required
def form(request):
    if request.method == 'POST':
        book_name_form = request.POST['book_name']
        book_auth_form = request.POST['auth_name']
        book_price_form = request.POST['book_price']
        book_type_form = request.POST['book_type']
        publisher_form = request.POST['publisher']
        published_on_form = request.POST['published_on']
        insert_data = Lib_Man_Sys_Table.objects.create(book_name=book_name_form,auth_name=book_auth_form,book_price=book_price_form,book_type=book_type_form,publisher=publisher_form,published_on=published_on_form)
        insert_data.save()
        return redirect('/data')
    return render(request,'form.html')


@login_required
def update(request,tid):
    if request.method == 'POST':
        book_name_form = request.POST['book_name']
        book_auth_form = request.POST['auth_name']
        book_price_form = request.POST['book_price']
        book_type_form = request.POST['book_type']
        publisher_form = request.POST['publisher']
        published_on_form = request.POST['published_on']
        insert_data = Lib_Man_Sys_Table.objects.filter(id=tid)
        insert_data.update(id=tid,book_name=book_name_form,auth_name=book_auth_form,book_price=book_price_form,book_type=book_type_form,publisher=publisher_form,published_on=published_on_form,active='y')
        return redirect ('/')
    else:
        content = {}
        content['data'] = Lib_Man_Sys_Table.objects.get(id=tid)
        return render(request,'update.html',content)


#permissions
@login_required
def to_archive(request,tid):
    archive = Lib_Man_Sys_Table.objects.filter(id=tid)
    archive.update(active='n')
    return redirect ('/')

@login_required
def archive_data(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='n')
    data = {'datas':datas}

    return render(request,'archived.html',data)

@login_required
def restore(request,tid):
    archive = Lib_Man_Sys_Table.objects.filter(id=tid)
    archive.update(active='y')
    return redirect('/archive_data')

@login_required
def delete(request,tid):
    delete = Lib_Man_Sys_Table.objects.filter(id=tid)
    delete.delete()
    return redirect('/')


# sort_by
@login_required
def sort_by_price(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('book_price')
    data = {'datas':datas}
    return redirect('/data')
    return render(request,'data.html',data)

@login_required
def sort_by_price_rev(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('-book_price')
    data = {'datas':datas}
    return render(request,'data.html',data)

@login_required
def sort_by_authorname(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('auth_name')
    data = {'datas':datas}
    return render(request,'data.html',data)

@login_required
def sort_by_authorname_rev(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('-auth_name')
    data = {'datas':datas}
    return render(request,'data.html',data)

@login_required
def sort_by_bookname(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('book_name')
    data = {'datas':datas}
    return render(request,'data.html',data)
@login_required
def sort_by_bookname_rev(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('-book_name')
    data = {'datas':datas}
    return render(request,'data.html',data)

@login_required
def sort_by_type(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('book_type')
    data = {'datas':datas}
    return render(request,'data.html',data)

@login_required
def sort_by_publisher(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('publisher')
    data = {'datas':datas}
    return render(request,'data.html',data)

@login_required
def sort_by_published_on(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('published_on')
    data = {'datas':datas}
    return render(request,'data.html',data)



@login_required
def real_myth(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').filter(book_type='Real Myth')
    data = {'datas':datas}
    return render(request,'data.html',data)

@login_required
def non_fiction(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').filter(book_type='Non-Fiction')
    data = {'datas':datas}
    return render(request,'data.html',data)

@login_required
def edited(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').filter(book_type='edited')
    data = {'datas':datas}
    return render(request,'data.html',data)

@login_required
def reference(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').filter(book_type='reference')
    data = {'datas':datas}
    return render(request,'data.html',data)

@login_required
def fiction(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').filter(book_type='fiction')
    data = {'datas':datas}
    return render(request,'data.html',data)
