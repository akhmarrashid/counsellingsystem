from django.db import models
from django.contrib.auth.models import User

def default_admin_image():
    return "default.png"

def default_staff_image():
    return "default.png"

def default_student_image():
    return "default.png"

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]

ISSUE_CHOICES = [
    ('akademik', 'Akademik'),
    ('pergaulan', 'Pergaulan'),
    ('penyesuaian diri', 'Penyesuaian Diri'),
    ('kewangan', 'Kewangan'),
    ('disiplin', 'Disiplin'),
    ('keluarga', 'Keluarga'),
]

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adminPhoneno = models.CharField(max_length=12,null=True)
    adminImage = models.ImageField(upload_to="admin_images/",null=True,blank=True,default=default_admin_image)

    @property
    def adminName(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.adminName


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staffName = models.CharField(max_length=100, null=True)
    staffPhoneno = models.CharField(max_length=12,null=True)
    unit = models.CharField(max_length=50,null=True)
    staffImage = models.ImageField(upload_to="staff_images/",null=True,blank=True,default=default_staff_image)

    @property
    def staffName(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.staffName


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=100, null=True)
    stuIdNo = models.CharField(max_length=11,null=True)
    gender = models.TextField(max_length=6,null=True)
    stuPhoneno = models.CharField(max_length=12,null=True)
    stuIcNo = models.CharField(max_length=12,null=True)
    course = models.CharField(max_length=100,null=True)
    semester = models.SmallIntegerField(null=True)
    mentor = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    stuImage = models.ImageField(upload_to="student_images/",null=True,blank=True,default=default_student_image)
    race = models.CharField(max_length=10,null=True)
    religion = models.CharField(max_length=20,null=True)
    guardian = models.CharField(max_length=12,null=True)
    
    @property
    def studentName(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.studentName

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    ISSUE_CHOICES = [
        ('akademik', 'Akademik'),
        ('pergaulan', 'Pergaulan'),
        ('penyesuaian diri', 'Penyesuaian Diri'),
        ('kewangan', 'Kewangan'),
        ('disiplin', 'Disiplin'),
        ('keluarga', 'Keluarga'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE,  null=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE,  null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending',  null=True)
    issue = models.CharField(max_length=50, choices=ISSUE_CHOICES, null=True)

    def __str__(self):
        return f"Appointment #{self.id} - {self.student.user.get_full_name()} with {self.admin.user.get_full_name()}"
    
class Referral(models.Model):    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    ISSUE_CHOICES = [
        ('akademik', 'Akademik'),
        ('pergaulan', 'Pergaulan'),
        ('penyesuaian diri', 'Penyesuaian Diri'),
        ('kewangan', 'Kewangan'),
        ('disiplin', 'Disiplin'),
        ('keluarga', 'Keluarga'),
    ]
    counselor = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    issue = models.CharField(max_length=50, choices=ISSUE_CHOICES, null=True)
    appointment_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending',  null=True)
    approved_by = models.ForeignKey(User, related_name='approved_by', null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"Referral for {self.student.user.get_full_name()} by {self.staff.user.get_full_name()}"

class SessionDetail(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, null=True, blank=True)
    referral = models.OneToOneField(Referral, on_delete=models.CASCADE, null=True, blank=True)
    clientBackground = models.TextField()
    mattersPresented = models.TextField()
    action = models.TextField()

    def __str__(self):
        if self.appointment:
            return f"Session Detail for Appointment #{self.appointment.appointmentId}"
        elif self.referral:
            return f"Session Detail for Referral #{self.referral.referralId}"
        else:
            return "Session Detail"

    class Meta:
        verbose_name_plural = "Session Details"
