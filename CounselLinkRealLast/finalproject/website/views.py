from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import AdminLoginForm, StaffLoginForm, StudentLoginForm, AdminCreationForm, AdminUpdateForm, StudentCreationForm, StudentUpdateForm, StaffCreationForm, StaffUpdateForm, AppointmentForm, ReferralForm
from .models import Admin, Student, Staff, Appointment, Referral, SessionDetail

#GENERAL


#LOGIN----------------------------------------------------------------------------------------------------------------------------------------------------------
def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user:
                login(request, user)
                return redirect('dashboard_admin')
            else:
                form.add_error(None, 'Invalid credentials or not an admin user')
    else:
        form = AdminLoginForm()
    return render(request, 'admin/loginAdmin.html', {'form': form})

def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    staff = Staff.objects.get(user=user)
                    login(request, user)
                    return redirect('dashboard_staff')
                except Staff.DoesNotExist:
                    form.add_error(None, 'Invalid credentials')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = StaffLoginForm()
    return render(request, 'staff/loginStaff.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    student = Student.objects.get(user=user)
                    login(request, user)
                    return redirect('dashboard_student')
                except Student.DoesNotExist:
                    form.add_error(None, 'Invalid credentials')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = StudentLoginForm()
    return render(request, 'student/loginStudent.html', {'form': form})

#DASHBOARD---------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required
def dashboard_admin(request):
    admin_user = Admin.objects.get(user=request.user)  # Fetch Admin instance
    context = {
        'admin': admin_user,
        'admin': request.user.admin

    }
    return render(request, 'admin/dashboardAdmin.html', context)

def dashboard_staff(request):
    return render(request, 'staff/dashboardStaff.html')

def dashboard_student(request):
    return render(request, 'student/dashboardStudent.html')

#PROFILE---------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required
def profile_admin(request):
    admins = Admin.objects.all()
    admin_user = Admin.objects.get(user=request.user)
    context = {
        'admins': admins,
        'admin': admin_user,
        'admin': request.user.admin
    }
    return render(request, 'admin/profileAdmin.html', context)

@login_required
def profile_student(request):
    students = Student.objects.all()
    student_user = Student.objects.get(user=request.user) 
    context = {
        'students': students,
        'student': student_user,
        'student': request.user.student
    }
    return render(request, 'student/profileStudent.html', context)

@login_required
def profile_staff(request):
    staffs = Staff.objects.all()
    staff_user = Staff.objects.get(user=request.user) 
    context = {
        'staffs': staffs,
        'staff': staff_user,
        'staff': request.user.staff
    }
    return render(request, 'staff/profileStaff.html', context)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#ADMIN
@login_required
def create_admin(request):
    admins = Admin.objects.all()
    if request.method == 'POST':
        form = AdminCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_list')
    else:
        form = AdminCreationForm()

    context = {
        'admins': admins,
        'admin': request.user.admin,
        'form': form,
    }
    return render(request, 'admin/createAdmin.html', context)

@login_required
def admin_list(request):
    admins = Admin.objects.all()
    context = {
        'admins': admins,
        'admin': request.user.admin
    }
    return render(request, 'admin/adminList.html', context)

@login_required
def admin_detail(request, username):
    user = get_object_or_404(User, username=username)
    admin = get_object_or_404(Admin, user=user)

    if request.method == 'POST':
        form = AdminUpdateForm(request.POST, request.FILES, instance=user)
        form.fields['adminPhoneno'].initial = admin.adminPhoneno
        form.fields['adminImage'].initial = admin.adminImage
        if form.is_valid():
            form.save()
            return redirect('admin_list')
        else:
            print(form.errors)
    else:
        form = AdminUpdateForm(instance=user, initial={
            'adminPhoneno': admin.adminPhoneno,
            'adminImage': admin.adminImage,
        })

    context = {
        'admin': admin,
        'user': request.user,
        'form': form,
    }
    return render(request, 'admin/adminDetail.html', context)

@login_required
def delete_admin(request, username):
    user = get_object_or_404(User, username=username)
    admin = get_object_or_404(Admin, user=user)
    if not user.is_superuser and not user == request.user:
        user.delete()
    return redirect('admin_list')

@login_required
def create_staff(request):
    if request.method == 'POST':
        form = StaffCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
        else:
            print(form.errors) 
    else:
        form = StaffCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'admin/createStaff.html', context)

@login_required
def staff_list(request):
    staffs = Staff.objects.all()
    context = {
        'staffs': staffs,
        'user': request.user
    }
    return render(request, 'admin/staffList.html', context)

@login_required
def staff_detail(request, username):
    user = get_object_or_404(User, username=username)
    staff = get_object_or_404(Staff, user=user)

    if request.method == 'POST':
        form = StaffUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffUpdateForm(instance=user)

    context = {
        'staff': staff,
        'user': request.user,
        'form': form,
    }
    return render(request, 'admin/staffDetail.html', context)

@login_required
def delete_staff(request, username):
    user = get_object_or_404(User, username=username)
    staff = get_object_or_404(Staff, user=user)
    user.delete()
    return redirect('staff_list')

@login_required
def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'user': request.user
    }
    return render(request, 'admin/studentList.html', context)

@login_required
def create_student(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            print(form.errors) 
    else:
        form = StudentCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'admin/createStudent.html', context)

@login_required
def student_detail(request, username):
    user = get_object_or_404(User, username=username)
    student = get_object_or_404(Student, user=user)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=user)
        form.fields['stuPhoneno'].initial = student.stuPhoneno
        form.fields['stuImage'].initial = student.stuImage
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentUpdateForm(instance=user, initial={
            'stuPhoneno': student.stuPhoneno,
            'stuImage': student.stuImage,
        })

    context = {
        'student': student,
        'user': request.user,
        'form': form,
    }
    return render(request, 'admin/studentDetail.html', context)

@login_required
def delete_student(request, username):
    user = get_object_or_404(User, username=username)
    student = get_object_or_404(Student, user=user)
    user.delete()
    return redirect('student_list')

@login_required
def manage_appointment(request):
    if hasattr(request.user, 'admin'):
        appointments = Appointment.objects.filter(admin=request.user.admin)
    else:
        appointments = []
    referrals = Referral.objects.filter(status='pending')
    approved_referrals = Referral.objects.filter(status='approved', approved_by=request.user)

    context = {
        'appointments': appointments,
        'referrals': referrals,
        'approved_referrals': approved_referrals,
    }
    return render(request, 'admin/manageAppointment.html', context)

@login_required
def update_appointment_status(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if hasattr(request.user, 'admin'):
        if request.method == 'POST':
            new_status = request.POST.get('status')
            if new_status in dict(Appointment.STATUS_CHOICES).keys():
                appointment.status = new_status
                appointment.save()
                return redirect('manage_appointment')
    return redirect('manage_appointment')

@login_required
def update_referral_status(request, referral_id):
    if request.method == 'POST':
        referral = get_object_or_404(Referral, id=referral_id)
        new_status = request.POST.get('status')
        referral.status = new_status
        if new_status == 'approved':
            referral.approved_by = request.user
        else:
            referral.approved_by = None
        referral.save()
        return redirect('manage_appointment')
    return redirect('manage_appointment')
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#STAFF

@login_required
def refer(request):
    if hasattr(request.user, 'staff'):
        if request.method == 'POST':
            form = ReferralForm(request.POST)
            if form.is_valid():
                referral = form.save(commit=False)
                referral.staff = request.user.staff
                referral.save()
                return redirect('dashboard_staff')
        else:
            form = ReferralForm()
        return render(request, 'staff/refer.html', {'form': form})
    return redirect('referral_list')

@login_required
def referral_list(request):
    if hasattr(request.user, 'staff'):
        referrals = Referral.objects.filter(staff=request.user.staff)
        return render(request, 'staff/referralList.html', {'referrals': referrals})
    return redirect('referral_list')

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#STUDENT
@login_required
def appointment_student(request):
    appointments = Appointment.objects.filter(student=request.user.student)
    return render(request, 'student/appointmentStudent.html', {'appointments': appointments})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.student = request.user.student
            appointment.status = 'Pending' 
            appointment.save()
            return redirect('appointment_student')
    else:
        form = AppointmentForm()
    return render(request, 'student/bookAppointment.html', {'form': form})


#IMPROPER
def faq_staff(request):
    return render(request, 'staff/faqStaff.html')

def faq_student(request):
    return render(request, 'student/faqStudent.html')

def session_detail(request):
    return render(request, 'admin/sessionDetail.html')