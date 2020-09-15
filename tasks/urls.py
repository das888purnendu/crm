from django.contrib import admin
from django.urls import path,include,re_path
from . import views
import re

urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("registration",views.registration,name="registration"),
    path("reg_form",views.reg_form,name="reg_form"),
    path("login_form",views.login_form,name="login_form"),
    path("success",views.success,name="success"),
    path("admin-dashboard",views.admin_dashboard,name="admin-dashboard"),
    path("admin-add-user",views.admin_add_user,name="admin-add-user"),
    path("admin-all-users",views.admin_all_users,name="admin-all-users"),
    path("admin-profile-update",views.admin_profile_update,name="admin-profile-update"),
    path("admin-update-user",views.admin_update_user,name="admin-update-user"),
    path("admin_profile_update_form",views.admin_profile_update_form,name="admin_profile_update_form"),
    path("admin_profile_photo_update",views.admin_profile_photo_update,name="admin_profile_photo_update"),
    path("ajax_call_delete_user",views.ajax_call_delete_user,name="ajax_call_delete_user"),
    path("profile_edit_by_get/<int:id>", views.profile_edit_by_get, name='profile_edit_by_get'),
    path("user_profile_update_form",views.user_profile_update_form,name="user_profile_update_form"),
    path("user_profile_photo_update",views.user_profile_photo_update,name="user_profile_photo_update"),
    path("admin_new_user_profile_form",views.admin_new_user_profile_form,name="admin_new_user_profile_form"),
    
]