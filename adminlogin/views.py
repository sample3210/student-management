from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseRedirect, HttpResponseRedirect
from .models import Student
from django.contrib import messages
from .forms import StudentForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Q
def adminclick_view(request):
    if request.user.is_authenticated:
        return redirect('admin-dashboard')
    return redirect('adminlogin')

def afterlogin_view(request):
        return redirect('admin-dashboard')
 
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    return render(request,'admin/dashboard.html')

def admin_404(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')
def index(request):
   
    return render(request,'login.html')

@login_required(login_url='adminlogin')
def admin_addstudent_view(request):
     if request.method == 'POST':
        # create a new student object
        student = Student()
        # set the fields from the form data
        student.name = request.POST['name']
        student.address = request.POST['address']
        student.fathername = request.POST['fathername']
        student.dob = request.POST['dob']
        student.gender = request.POST['gender']
        student.contact_no = request.POST['contact_no']
        student.class_name = request.POST['class_name']
        student.remarks = request.POST['text']
        # save the student object to the database
        student.save()
        # redirect to the success page
        return redirect('admin-studentlist')
     else:
        return render(request, 'admin/registration.html')

@login_required(login_url='adminlogin')
def admin_studentlist_view(request):
   student_list = Student.objects.order_by('id') # Order the queryset by 'id'
   paginator = Paginator(student_list, 2) # Show 2 students per page
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   return render(request, 'admin/studentlist.html', {'page_obj': page_obj})

@login_required(login_url='adminlogin')
def admin_studentedit_view(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('admin-studentlist')
    else:
        form = StudentForm(instance=student)

    context = {'form': form}
    return render(request, 'admin/edit_student.html', context)



def admin_password_reset(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        new_password = request.POST['new_password']


        try:
            # Check if the username_or_email exists in the User model (you can customize this to your actual user model)
            user = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
        except User.DoesNotExist:
            # If the user is not found, show an error message
            messages.error(request, 'Admin not found with the provided username or email.')
            return redirect('admin_password_reset')


        # Update the user's password
        user.set_password(new_password)
        user.save()


        messages.success(request, 'Password reset successful.')
        return redirect('adminlogin')  # Redirect to login page or any other appropriate page


    return render(request, 'admin/password_reset.html')
