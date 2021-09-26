from rest_framework import serializers, status
from .models import Address, UserProfile, Leave, Payroll
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from collections import OrderedDict
from django.utils import timezone 
import json


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		try:
			username = User.objects.get(email=attrs['username']).username
			attrs['username'] = username
		except:
			username = attrs['username']
		user = authenticate(username=username, password=attrs['password'])
		if user is not None:
			if user.is_active: 
				data = super().validate(attrs)
				data = {}
				refresh = self.get_token(self.user)
				refresh['username'] = self.user.username
				try:
					obj = UserProfile.objects.get(user=self.user)
					refresh['role'] = obj.role
					data["refresh"] = str(refresh)
					data["access"] = str(refresh.access_token)
					data["user_id"] = self.user.id
					data['user_name']= self.user.username
					data["role"] = obj.role
					data['first_name']= self.user.first_name
					data['last_name']= self.user.last_name
					if obj.photo:
						data['profile_pic']= obj.photo.url
					else:
						data['profile_pic']= None
				except Exception as e:
					raise serializers.ValidationError('User verification failed!')
				return data
			else:
				raise serializers.ValidationError('Account is Blocked')
		else:
			raise serializers.ValidationError('Incorrect userid/email and password combination!')


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'email',)
	
	def create(self, validated_data):
		# create user 
		user = User.objects.create(
			username = validated_data['username'],
			email = validated_data['email'],
			first_name = validated_data['first_name'],
			last_name = validated_data['last_name'],
		)
		user.set_password('test@123')
		user.save()
		profile_data = json.loads(self.initial_data['profile'])
		# create profile
		profile = UserProfile.objects.create(
			user = user,
			role = profile_data['role'],
			gender = profile_data['gender'],
			description = profile_data['description'],
		)

		return user


class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, required=True)
	address = AddressSerializer()
	class Meta:
		model = UserProfile
		fields = ('user', 'role', 'gender', 'description', 'dob', 'address', 'photo')

class UserProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer
	class Meta:
		model = UserProfile
		fields = ('user', 'role', 'gender', 'description', 'dob', 'address', 'photo')

class LeaveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leave
		fields = '__all__'

	def save(self, instance):
		super().save()

class EmployeePayrollSerializer(serializers.ModelSerializer):
	user = UserProfileSerializer(many=False, required=True)
	leaves = LeaveSerializer()
	class Meta:
		model = Payroll
		fields = ('user', 'salary', 'leaves')


