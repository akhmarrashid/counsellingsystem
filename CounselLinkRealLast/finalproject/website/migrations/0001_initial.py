# Generated by Django 4.2.4 on 2024-07-10 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminPhoneno', models.CharField(max_length=12, null=True)),
                ('adminImage', models.ImageField(blank=True, default=website.models.default_admin_image, null=True, upload_to='admin_images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='Pending', max_length=20, null=True)),
                ('issue', models.CharField(choices=[('akademik', 'Akademik'), ('pergaulan', 'Pergaulan'), ('penyesuaian diri', 'Penyesuaian Diri'), ('kewangan', 'Kewangan'), ('disiplin', 'Disiplin'), ('keluarga', 'Keluarga')], max_length=50, null=True)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=20)),
                ('issue', models.CharField(choices=[('akademik', 'Akademik'), ('pergaulan', 'Pergaulan'), ('penyesuaian diri', 'Penyesuaian Diri'), ('kewangan', 'Kewangan'), ('disiplin', 'Disiplin'), ('keluarga', 'Keluarga')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuIdNo', models.CharField(max_length=11, null=True)),
                ('gender', models.TextField(max_length=6, null=True)),
                ('stuPhoneno', models.CharField(max_length=12, null=True)),
                ('stuIcNo', models.CharField(max_length=12, null=True)),
                ('course', models.CharField(max_length=100, null=True)),
                ('semester', models.SmallIntegerField(null=True)),
                ('mentor', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('stuImage', models.ImageField(blank=True, default=website.models.default_student_image, null=True, upload_to='student_images/')),
                ('race', models.CharField(max_length=10, null=True)),
                ('religion', models.CharField(max_length=20, null=True)),
                ('guardian', models.CharField(max_length=12, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffPhoneno', models.CharField(max_length=12, null=True)),
                ('unit', models.CharField(max_length=50, null=True)),
                ('staffImage', models.ImageField(blank=True, default=website.models.default_staff_image, null=True, upload_to='staff_images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SessionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientBackground', models.TextField()),
                ('mattersPresented', models.TextField()),
                ('action', models.TextField()),
                ('appointment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.appointment')),
                ('referral', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.referral')),
            ],
            options={
                'verbose_name_plural': 'Session Details',
            },
        ),
        migrations.AddField(
            model_name='referral',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.staff'),
        ),
        migrations.AddField(
            model_name='referral',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.student'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.student'),
        ),
    ]
