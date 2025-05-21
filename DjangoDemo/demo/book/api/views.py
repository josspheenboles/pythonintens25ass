from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serlizer import *
from ..models import *

@api_view(['GET'])
def getall(request):
    books=Book2.getall()
    books_serlized=BookSerlizer(books,many=True)
    return Response(
        data=books_serlized.data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def getbyid(request,id):
    book=Book2.get_by_id(id)
    BookSerlized=BookSerlizer(book)
    return Response(
        data=BookSerlized.data,
        status=status.HTTP_200_OK
    )
