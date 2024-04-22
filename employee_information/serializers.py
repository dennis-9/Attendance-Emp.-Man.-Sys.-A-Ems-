from rest_framework import serializers
from .models import Fingerprint, Employees

class FingerprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fingerprint
        fields = ('id', 'finger_data', 'employee_id', 'created_at', 'updated_at', 'scan_time', 'scan_status')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id', 'firstname', 'lastname', 'department_id', 'position_id')
        
        