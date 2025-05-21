from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serlizer import *
from ..models import *
from rest_framework.views import  APIView
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.pagination import  PageNumberPagination



class BookCreateAPIView(CreateAPIView):
        queryset = Book2.getall()
        serializer_class = BookSerlizer
        # model=Book2

class BookPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100

class BookList(ListAPIView):
    serializer_class = BookSerlizer
    queryset = Book2.getall()
    pagination_class =BookPagination

#get by id,put,patch,delete
class BookClass2(APIView):
    def get(self,request, id):
        try:
            book = get_object_or_404(Book2, pk=id)

            BookSerlized = BookSerlizer(book)
            return Response(
                data=BookSerlized.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request,id):
        try:
            book = get_object_or_404(Book2, pk=id)
            BookSerlizer().update(instance=book,validated_data=request.data)
            return Response(data={'msg','book updated'},
                            status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self,request, id):
        try:
            book = get_object_or_404(Book2, pk=id)
            book.delete()
            return Response(
                {"message": "Book deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

#get,post
class BookClass(APIView):
    def get(self,request):
        books = Book2.getall()
        books_serlized = BookSerlizer(books, many=True)
        return Response(
            data=books_serlized.data,
            status=status.HTTP_200_OK
        )
    def get(self,request):
        books = Book2.getall()
        books_serlized = BookSerlizer(books, many=True)
        return Response(
            data=books_serlized.data,
            status=status.HTTP_200_OK
        )

    def post(self,request):
        # deserlize data
        serlizerdData = BookSerlizer(data=request.data)
        if serlizerdData.is_valid():
            serlizerdData.save()
            return Response(
                data={'msg': f'book created ' + str(serlizerdData.data['id'])},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={'msg': serlizerdData.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )



@api_view(['GET','POST'])
def getall(request):
    if request.method == 'GET':
        books=Book2.getall()
        books_serlized=BookSerlizer(books,many=True)
        return Response(
            data=books_serlized.data,
            status=status.HTTP_200_OK
        )
    else:
        # deserlize data
        serlizerdData = BookSerlizer(data=request.data)
        if serlizerdData.is_valid():
            serlizerdData.save()
            return Response(
                data={'msg': f'book created ' + str(serlizerdData.data['id'])},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={'msg': serlizerdData.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )



@api_view(['GET','DELETE','PUT'])
def getbyid(request,id):
    if request.method=='GET':
        book=Book2.get_by_id(id)
        BookSerlized=BookSerlizer(book)
        return Response(
            data=BookSerlized.data,
            status=status.HTTP_200_OK
        )
    elif request.method=='DELETE':
        try:
            book = get_object_or_404(Book2, pk=id)
            book.delete()
            return Response(
                {"message": "Book deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    elif request.method == 'PUT':
        try:
            book = get_object_or_404(Book2, pk=id)
            BookSerlizer().update(instance=book,validated_data=request.data)
            return Response(data={'msg','book updated'},
                            status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )



