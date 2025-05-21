from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serlizer import *
from ..models import *

def getall(request):
    books=Book2.getall()
    books_serlized=BookSerlizer(books,many=True)
    return Response(
        data=books_serlized.data,
        status=status.HTTP_200_OK
    )
