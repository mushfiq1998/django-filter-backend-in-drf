from .models import Student
from .serializers import StudentSerializer 
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class StudentList(ListAPIView):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    # Define the fields based on which filtering will be applied
    # Here, filtering will be based on city field
    # filterset_fields = ['city']
    filterset_fields = ['name', 'city']
