from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['id', 'category', 'title','description','tech_stack','github_link','live_link','image','created_at']
        