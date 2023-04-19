
from django.urls import path,include
from adminlogin import views
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib import admin
from adminlogin.views import index, adminclick_view, admin_dashboard_view, admin_addstudent_view, admin_studentlist_view,admin_studentedit_view,admin_password_reset,admin_404

urlpatterns = [
    
    path('', LoginView.as_view(template_name='admin/login.html'),name='adminlogin'),
     # add these lines
    path('adminclick', views.adminclick_view),
  
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin-dashboard', admin_dashboard_view, name='admin-dashboard'),
    path('admin-addstudent', admin_addstudent_view, name='admin-addstudent'),
    path('admin-studentlist', admin_studentlist_view, name='admin-studentlist'),
    path('admin-studentedit/<int:pk>/', admin_studentedit_view, name='admin-studentedit'),
  path('admin/password/reset/', admin_password_reset, name='admin_password_reset'),
    path('admin/404', admin_404),
    

]
