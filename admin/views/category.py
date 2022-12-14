
from django.http import Http404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Category, Product
from admin.serializers import CategorySerializer, ProductSerializer

from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class CategoryView(APIView):

    '''
    /admin/categories/<category-slug>/
    '''

    def get(self, request, slug):
        
        try:
            category = Category.objects.get(slug=slug)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category)


        products = Product.objects.filter(category=category).order_by('created_at')

        pagination = CustomPageNumberPagination()
        page = pagination.paginate_queryset(products, request)
        pr_serializer = ProductSerializer(page, many=True)

        return pagination.get_paginated_response({
            'category': serializer.data,
            'products': pr_serializer.data,
            })


    def put(self, request, slug):

        try:
            category = Category.objects.get(slug=slug)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data

        parent_category_id = data.get('parent_category_id')

        if parent_category_id:
            try:
                parent_category = Category.objects.get(id=parent_category_id)

                category.parent_category = parent_category

            except Category.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        category.name        = data.get('name', category.name)
        category.slug        = data.get('slug', category.slug)
        category.description = data.get('description', category.description)

        category.save()

        serializer = CategorySerializer(category)

        return Response({
            'category': serializer.data
            })
 

    def delete(self, request, slug):

        try:
            category = Category.objects.get(slug=slug)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        category.is_active = False
        category.save()

        serializer = CategorySerializer(category)

        return Response({
            'category': serializer.data
            })
 






