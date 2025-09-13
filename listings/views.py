from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ListingListView(generics.ListAPIView):
    """
    API endpoint for listing all travel listings
    """
    
    @swagger_auto_schema(
        operation_description="Get all travel listings",
        responses={200: "List of travel listings"}
    )
    def get(self, request, *args, **kwargs):
        return Response({
            "message": "Welcome to ALX Travel App API",
            "listings": []
        }, status=status.HTTP_200_OK)

class ListingDetailView(generics.RetrieveAPIView):
    """
    API endpoint for retrieving a specific travel listing
    """
    
    @swagger_auto_schema(
        operation_description="Get a specific travel listing by ID",
        responses={200: "Travel listing details"}
    )
    def get(self, request, pk, *args, **kwargs):
        return Response({
            "id": pk,
            "message": f"Listing {pk} details will be implemented"
        }, status=status.HTTP_200_OK)