from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import UserRateThrottle
from django.contrib.auth import authenticate
from .models import Document
from .serializers import DocumentSerializer, UserLoginSerializer

class LoginThrottle(UserRateThrottle):
    rate = '5/min'

@api_view(['POST'])
@throttle_classes([LoginThrottle])
def login_user(request, id):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Document.objects.filter(user=self.request.user)

        sort_by = self.request.query_params.get('sort_by')
        if sort_by in ['created', 'updated']:
            queryset = queryset.order_by(sort_by)

        tag_id = self.request.query_params.get('tag')
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)