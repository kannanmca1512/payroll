# Generated by Django 3.2.7 on 2021-09-26 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/profile_pic/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, choices=[('ADMIN', 'ADMIN'), ('EMPLOYEE', 'EMPLOYEE'), ('STAFF', 'STAFF')], max_length=10, null=True),
        ),
    ]
