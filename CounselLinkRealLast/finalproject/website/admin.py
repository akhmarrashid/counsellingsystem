from django.contrib import admin
from .models import Admin, Staff, Student, Appointment, Referral, SessionDetail

#user 1 (username: akhmarrashid, password: WTJ1450vfb2593)

admin.site.register(Admin)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Appointment)
admin.site.register(Referral)
admin.site.register(SessionDetail)