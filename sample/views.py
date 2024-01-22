from django.shortcuts import render,get_object_or_404
from .models import Book, CustomUser
from django.contrib.auth import authenticate,login
from .serializers import BookSerializer, BookNameSerializer, CustomUserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status 

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import  AllowAny
# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def RegisterUser(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            if CustomUser.objects.filter(username=username).exists():
                 return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

            
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def user_login(request):

    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            print(username,password)
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
                

    

    
        



@api_view(['POST', 'GET'])
def BookView(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def SingleBook(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST', 'GET'])
def BookName(request):
    if request.method == 'POST':
        serializer = BookNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        books = Book.objects.all()
        serializer = BookNameSerializer(books, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



    

    

