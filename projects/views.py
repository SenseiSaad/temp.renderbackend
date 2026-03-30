from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import status



@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def oneproject(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def allprojects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])

def createproject(request):
    serializers=ProjectSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST )

@api_view(['PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def updateproject(request, pk):
    project = Project.objects.get(id=pk)
    serializers = ProjectSerializer(project, data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def deleteproject(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return Response({'message': 'Project was deleted'})