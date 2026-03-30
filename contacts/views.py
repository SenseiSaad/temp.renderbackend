from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from .models import Contact
from rest_framework.permissions import AllowAny as any
from .serializers import ContactSerializer


@api_view(['POST'])
@permission_classes([any])
def create_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)