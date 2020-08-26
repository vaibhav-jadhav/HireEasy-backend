from rest_framework import serializers
from .models import Jobs,  Applications,Interview
class JObsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields = '__all__'
class  ApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Applications
        fields = '__all__'
class  InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Interview
        fields = '__all__'
        
        
        
        
        
        
