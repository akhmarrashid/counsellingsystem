# Generated by Django 4.2.4 on 2024-07-10 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referral',
            old_name='date',
            new_name='appointment_date',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='time',
        ),
        migrations.AddField(
            model_name='referral',
            name='counselor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.admin'),
        ),
        migrations.AlterField(
            model_name='referral',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='Pending', max_length=20, null=True),
        ),
    ]
