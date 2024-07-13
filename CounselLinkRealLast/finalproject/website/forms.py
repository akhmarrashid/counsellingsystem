from django import forms
from django.contrib.auth.models import User
from .models import Admin, Student, Staff, Appointment, Referral, SessionDetail

class AdminLoginForm(forms.Form):
    username = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'}))
    password = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))

class StaffLoginForm(forms.Form):
    username = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'}))
    password = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))

class StudentLoginForm(forms.Form):
    username = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Student ID'}))
    password = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

class AdminCreationForm(forms.ModelForm):
    adminPhoneno = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    adminImage = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super(AdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            admin = Admin(user=user, adminPhoneno=self.cleaned_data.get('adminPhoneno'), adminImage=self.cleaned_data.get('adminImage'))
            admin.save()
        return user

class AdminUpdateForm(forms.ModelForm):
    adminPhoneno = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    adminImage = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super(AdminUpdateForm, self).save(commit=False)
        if commit:
            user.save()
            if hasattr(user, 'admin'):
                admin = user.admin
            else:
                admin = Admin(user=user)
            admin.adminPhoneno = self.cleaned_data.get('adminPhoneno')
            admin.adminImage = self.cleaned_data.get('adminImage', admin.adminImage)
            admin.save()
        return user
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
class StudentCreationForm(forms.ModelForm):
    stuPhoneno = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    stuImage = forms.ImageField(required=False)
    stuIdNo = forms.CharField(max_length=11, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    course = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    semester = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-input'}))
    mentor = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super(StudentCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            student = Student(
                user=user,
                stuPhoneno=self.cleaned_data.get('stuPhoneno'),
                stuImage=self.cleaned_data.get('stuImage'),
                stuIdNo=self.cleaned_data.get('stuIdNo'),
                course=self.cleaned_data.get('course'),
                semester=self.cleaned_data.get('semester'),
                mentor=self.cleaned_data.get('mentor'),
            )
            student.save()
        return user
    

class StudentUpdateForm(forms.ModelForm):
    stuPhoneno = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    stuImage = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.fields['stuPhoneno'].initial = self.instance.student.stuPhoneno
        self.fields['stuImage'].initial = self.instance.student.stuImage

    def save(self, commit=True):
        user = super(StudentUpdateForm, self).save(commit=False)
        user.save()
        student = user.student
        student.stuPhoneno = self.cleaned_data.get('stuPhoneno', student.stuPhoneno)
        student.stuImage = self.cleaned_data.get('stuImage', student.stuImage)
        student.save()
        return user
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

class StaffCreationForm(forms.ModelForm):
    staffPhoneno = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    staffImage = forms.ImageField(required=False)
    unit = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super(StaffCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            staff = Staff(
                user=user,
                staffPhoneno=self.cleaned_data.get('staffPhoneno'),
                staffImage=self.cleaned_data.get('staffImage'),
                unit=self.cleaned_data.get('unit'),
            )
            staff.save()
        return user
    
class StaffUpdateForm(forms.ModelForm):
    staffPhoneno = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    staffImage = forms.ImageField(required=False)
    unit = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'unit']

    def __init__(self, *args, **kwargs):
        super(StaffUpdateForm, self).__init__(*args, **kwargs)
        if hasattr(self.instance, 'staff'):
            self.fields['staffPhoneno'].initial = self.instance.staff.staffPhoneno
            self.fields['staffImage'].initial = self.instance.staff.staffImage
            self.fields['unit'].initial = self.instance.staff.unit

    def save(self, commit=True):
        user = super(StaffUpdateForm, self).save(commit=False)
        if commit:
            user.save()
            if hasattr(user, 'staff'):
                staff = user.staff
            else:
                staff = Staff(user=user)
            staff.staffPhoneno = self.cleaned_data.get('staffPhoneno', staff.staffPhoneno)
            staff.staffImage = self.cleaned_data.get('staffImage', staff.staffImage)
            staff.unit = self.cleaned_data.get('unit', staff.unit)
            staff.save()
        return user
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class AppointmentForm(forms.ModelForm):
    admin = forms.ModelChoiceField(
        queryset=Admin.objects.all(),
        empty_label="Select a Counselor",
        widget=forms.Select(attrs={'class': 'form-control form-control-alternative'}),
        required=True,
        label='Counselor'
    )

    ISSUE_CHOICES = [
        ('akademik', 'Akademik'),
        ('pergaulan', 'Pergaulan'),
        ('penyesuaian diri', 'Penyesuaian Diri'),
        ('kewangan', 'Kewangan'),
        ('disiplin', 'Disiplin'),
        ('keluarga', 'Keluarga'),
    ]

    issue = forms.ChoiceField(
        choices=ISSUE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control form-control-alternative'}),
        required=True,
        label='Issue'
    )

    class Meta:
        model = Appointment
        fields = ['admin', 'date', 'time', 'issue']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-alternative'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-alternative'}),
        }

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['counselor', 'student', 'issue', 'appointment_date']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }