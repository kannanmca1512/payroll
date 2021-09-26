from django.shortcuts import render
from .models import UserProfile, Address, Payroll, Leave
from . serializers import (
	MyTokenObtainPairSerializer, EmployeeSerializer, EmployeePayrollSerializer, 
	LeaveSerializer, UserSerializer
)
from rest_framework import generics, permissions, serializers, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class LoginView(TokenObtainPairView):
	"""
	Login View with jWt token authentication
	"""
	serializer_class = MyTokenObtainPairSerializer


class EmpInfo(APIView):
	"""
		Enables the api to view the employee view by himself/herself.
	"""
	permission_classes = [permissions.IsAuthenticated]
	authentication_classes = [JWTAuthentication]
	def get(self, request):
		""" Get employee information with the user_id in employee's own credentials 
			(id in auth_user table)
		"""
		emp = UserProfile.objects.filter(user_id=request.user.id)
		if emp.count() == 0: # This might happen, if User does not have Employee fields
			return Response({ 'Error': 'Employee not found'})
		serialized_emp = EmployeeSerializer(emp, many=True)
		return Response({ 'employee': serialized_emp.data})


class GetAllEmps(APIView):
	"""
		Enables the api to view all the employees for an admin user.
	"""
	permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
	authentication_classes = [JWTAuthentication]
	def get(self, request):
		"""
			get all employees information
		"""
		emps = UserProfile.objects.all()
		if emps.count() == 0:
			return Response({ 'Error': 'Employees not found'})
		serialized_emps = EmployeeSerializer(emps, many=True)
		return Response({ 'employees': serialized_emps.data})


class EmpPayrollInfo(APIView):
	"""
		Enables the api to view the employee payroll view by himself/herself.
	"""
	permission_classes = [permissions.IsAuthenticated]
	authentication_classes = [JWTAuthentication]
	def get(self, request):
		""" Get employee information with the user_id in employee's own credentials 
			(id in auth_user table)
		"""
		emp = Payroll.objects.filter(user_id=request.user.id)
		if emp.count() == 0: # This might happen, if User does not have Employee fields
			return Response({ 'Error': 'Employee not found'})
		serialized_emp = EmployeePayrollSerializer(emp, many=True)
		return Response({ 'employee': serialized_emp.data})

class EmpViewAndUpdations(APIView):
	"""
		APiView class to admin user to view and modify employee's information.
	"""
	permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
	authentication_classes = [JWTAuthentication]

	def get(self, request, emp_id, format=None):
		"""Get employee information with the id in auth_user table"""
		emp = UserProfile.objects.filter(user_id=emp_id)
		if emp.count() == 0: # This might happen, if User does not have Employee fields
			return Response({ 'Error': 'Employee not found'})
		serialized_emp = EmployeeSerializer(emp, many=True)
		return Response({ 'employee': serialized_emp.data})


	def post(self, request, emp_id, format=None):
		"""
		Update employee information mainly leave
		"""

		emp = UserProfile.objects.filter(user_id=emp_id).first()
		if emp == None:
			return Response({ 'Error': 'Employee not found'})

		no_of_leave = int(request.POST.get('leaves'))
		leave_obj = Leave.objects.filter(user=emp).first()
		data = {}
		data.update(
			{
				'pending_leaves':int(leave_obj.pending_leaves) + int(no_of_leave)
			}
		)
		if no_of_leave != None:
			serialized_employee = LeaveSerializer(
				emp, 
				data=data,
				partial=True
			)

			if serialized_employee.is_valid():
				serialized_employee.save(emp)
				return Response({ 'employee': serialized_employee.data})
			else:
				return Response({ 'Error': 'Parameters not valid'})
		else:
			serialized_employee = EmployeeSerializer(emp)
			return Response({  'Error': 'Employee not updated'})


class EmpRegistration(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
	authentication_classes = [JWTAuthentication]
	serializer_class = UserSerializer

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)