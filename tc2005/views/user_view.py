from rest_framework import viewsets
from tc2005.models import User
from tc2005.serializers.user_serializer import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, status
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

'''
A viewset that provides default 
    `create()`,  /user POST
    `retrieve()`, /user/1 GET
    `update()`, /user/1 PUT
    `partial_update()`,  /user/1 PATCH
    `destroy()` /user/1 DELETE
    and `list()` /user GET
    actions.
'''


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all() # Select * from user;
    serializer_class = UserSerializer
    permission_classes =  ()
    authentication_classes = (SessionAuthentication, TokenAuthentication, )

    @action(methods=["GET"],  detail=False, serializer_class=LoginSerializer, permission_classes=[IsAuthenticated])
    def current_user(self, request):
    
        return Response({
            "user": str(request.user),
            'auth': str(request.auth),
            'role': bool(request.user.is_manager),
            "id": request.user.id,
        }, status=status.HTTP_200_OK) 


    @action(methods=["POST"],  detail=False, serializer_class=LoginSerializer, permission_classes=[AllowAny])
    def login(self, request):
    
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(): 
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            try:
                user = User.objects.get(email=email) # Select * From User Where email = ""
            except BaseException as e:
                raise ValidationError({"error": str(e)})
            
            if not check_password(password, user.password):
                raise ValidationError({"error": "Incorrect password"})
            
            user.last_login = timezone.now()
            user.save()

            token, created = Token.objects.get_or_create(user=user)
            print(token)

            return Response({"token":token.key}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
            

    # Signup
    def create(self, request):

        serializer = UserSerializer(data=request.data)
        user =  None

        if serializer.is_valid():
            user =  User.objects.create_user(
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            
            )
            
            print(user)
            
            user.save()
            response = UserSerializer(instance=user, context={'request': request} )

            return Response(response.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    
