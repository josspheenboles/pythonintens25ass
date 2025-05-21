from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serlizer import *
from ..models import *

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



@api_view(['GET'])
def getbyid(request,id):

        book=Book2.get_by_id(id)
        BookSerlized=BookSerlizer(book)
        return Response(
            data=BookSerlized.data,
            status=status.HTTP_200_OK
        )


# @api_view(['POST'])
# def createBook(request):
