from django.shortcuts import render

from django.http import HttpResponse # To return the response
from django.shortcuts import get_object_or_404  # To return 404 when object does not exist
from rest_framework.views import APIView  # Normal views can return API data
from rest_framework.response import Response # get status of a particular response
from rest_framework import status  # for status
from .models import employees  # name of my model
from .serializers import employeesSerializer  # Serializer

# Now create a class-based view which inherits our API views
class employeeList(APIView):

    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeesSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
