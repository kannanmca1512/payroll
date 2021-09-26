from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Address(models.Model):
	address_line_1 = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	address_line_2 = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	city = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	state = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	country = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	zip_code = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	phone_1 = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	phone_2 = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	fax = models.CharField(max_length=150, default=None, blank=True, null=True)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	GENDER_CHOICES = (
		('MALE', 'MALE'),
		('FEMALE', 'FEMALE'),
		('OTHERS', 'OTHERS'),
	)

	ROLE_CHOICES = (
		('ADMIN', 'ADMIN'),
		('EMPLOYEE', 'EMPLOYEE'),
		('MANAGER', 'MANAGER'),
		('HR_MANAGER', 'HR_MANAGER'),
	)
	role = models.CharField(choices=ROLE_CHOICES, null=True, blank=True, max_length=10)
	gender = models.CharField(
		max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	dob = models.DateTimeField(default=None, null=True, blank=True)
	address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, blank=True)
	photo = models.ImageField(upload_to='users/profile_pic/', blank=True)

	def __str__(self):
	   return self.user.email

class Leave(models.Model):
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
	available_leaves = models.IntegerField(default=24, null=True, blank=True)
	approved_leaves = models.IntegerField(default=0, null=True, blank=True)
	pending_leaves = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
	   return self.user.user.email

class Payroll(models.Model):
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
	salary = models.FloatField()
	leaves = models.OneToOneField(Leave, on_delete=models.CASCADE)

	def __str__(self):
	   return self.user.user.email
