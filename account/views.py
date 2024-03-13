from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Author, Publisher
from .serializer import AuthorSerializer, PublisherSerializer
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@api_view(['GET', 'POST'])
def getall_authors(request):
    """
    End point to return all the authors 
    or
    create a new one
    """
    authors = Author.objects.all()
    if request.method == 'GET':
        authors_serializer = AuthorSerializer(authors, many=True)
        return Response (authors_serializer.data, status=status.HTTP_200_OK)
    else:
        data = request.data
        author_serializer = AuthorSerializer(data=data)
        if author_serializer.is_valid():
            author_serializer.save()
            return Response({
                'Msg': 'New author added successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(author_serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])         -->Uncomment for authentication
def get_author_id(request, id):
    """
    Return the required author that called by ID
    or
    Update
    or 
    Delete
    When the api is called
    """
    try:
        author = Author.objects.get(id = id)
    except Author.DoesNotExist:
        return Response(
              {
            'Msg': 'Author not found'
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        author_serializer = AuthorSerializer(author)
        return Response(author_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        author.delete()
        return Response({
            'Msg': 'Author deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        data = request.data
        author_serializer = AuthorSerializer(instance=author, data=data)
        if author_serializer.is_valid():
            author_serializer.save()
            return Response({
                'Msg': 'Author updated successfully'
            }, status=status.HTTP_200_OK)
        return Response(author_serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        data = request.data
        author_serializer = AuthorSerializer(instance=author, data=data, partial=True)
        if author_serializer.is_valid():
            author_serializer.save()
            return Response({
            'Msg': 'Author updated successfully'
        }, status=status.HTTP_200_OK)
        return Response(author_serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
