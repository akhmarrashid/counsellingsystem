from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

    #LOGIN
    path("", views.student_login, name='student_login'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('staff-login/', views.staff_login, name='staff_login'),
    path('logout/', LogoutView.as_view(template_name='student/loginStudent.html'),name='logout'),

    #DASHBOARD
    path('dashboard-admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard-staff/', views.dashboard_staff, name='dashboard_staff'),
    path('dashboard-student/', views.dashboard_student, name='dashboard_student'),

    #PROFILE
    path('profile-admin/', views.profile_admin, name='profile_admin'),
    path('profile-staff/', views.profile_staff, name='profile_staff'),
    path('profile-student/', views.profile_student, name='profile_student'),

    #GENERAL

#-----------------------------------------------------------------------------------------------------------------

    #ADMIN
    path('admin-list/', views.admin_list, name='admin_list'),
    path('admin-create/', views.create_admin, name='create_admin'),
    path('admin-detail/<str:username>/', views.admin_detail, name='admin_detail'),
    path('admin-delete/<str:username>/', views.delete_admin, name='delete_admin'),
    path('staff-list/', views.staff_list, name='staff_list'),
    path('staff-create/', views.create_staff, name='create_staff'),
    path('staff-detail/<str:username>/', views.staff_detail, name='staff_detail'),
    path('staff-delete/<str:username>/', views.delete_staff, name='delete_staff'),
    path('student-list/', views.student_list, name='student_list'),
    path('student-create/', views.create_student, name='create_student'),
    path('student-detail/<str:username>/', views.student_detail, name='student_detail'),
    path('student-delete/<str:username>/', views.delete_student, name='delete_student'),
    path('manage-appointment/', views.manage_appointment, name='manage_appointment'),
    path('update-appointment-status/<int:appointment_id>/', views.update_appointment_status, name='update_appointment_status'),
    path('update_referral_status/<int:referral_id>/', views.update_referral_status, name='update_referral_status'),



    #STAFF
    path('refer/', views.refer, name='refer'),
    path('faq-staff/', views.faq_staff, name='faq_staff'),
    path('faq-student/', views.faq_student, name='faq_student'),

    #STUDENT
    path('appointment-student/', views.appointment_student, name='appointment_student'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),


    #IMPROPER
    path('referral-list/', views.referral_list, name='referral_list'),
    path('session-detail/', views.session_detail, name='session_detail'),

]