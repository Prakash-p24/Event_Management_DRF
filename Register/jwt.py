from rest_framework_simplejwt.tokens import RefreshToken


# def get_tokens_for_user(user):
#     """
#     Generates access and refresh tokens for a given user instance.
#     """
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }
# import jwt
# import datetime
# from django.conf import settings
# from django.contrib.auth.hashers import check_password
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from .models import User  # Your custom user model


# def CreateJWT(request):
#     username = request.data.get("user_name")
#     password = request.data.get("password")

#     try:
#         user = User.objects.get(user_name=username)
#     except User.DoesNotExist:
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#     # Check password (works for hashed passwords)
#     if not check_password(password, user.password):
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#     # Create JWT payload
#     payload = {
#         'id': str(user.id),  # UUID converted to string
#         'username': user.user_name,
#         'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
#         'iat': datetime.datetime.utcnow()
#     }

#     # Generate token
#     token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

#     return Response({'token': token}, status=status.HTTP_200_OK)
# from django.contrib.auth.backends import BaseBackend
# from .models import User

# class PlainTextBackend(BaseBackend):
#     def authenticate(self, request, user_name=None, password=None, **kwargs):
#         print("Authenticate called:", user_name, password)  # debug
#         try:
#             user = User.objects.get(user_name=user_name)
#             print("User found:", user)
#             if user.check_password(password):
#                 print("Password matched")
#                 return user
#             else:
#                 print("Password mismatch")
#         except User.DoesNotExist:
#             print("User does not exist")
#         return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
