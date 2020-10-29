from django_grpc_framework import mixins
from django_grpc_framework import generics

from google.protobuf import empty_pb2
from django_grpc_framework.services import Service

from book.models import Category, Publisher, Author, Book
from book.serializers import \
    CategoryProtoSerializer, \
    PublisherProtoSerializer, \
    AuthorProtoSerializer, \
    BookProtoSerializer


class CategoryService(generics.ModelService):
    queryset = Category.objects.all()
    serializer_class = CategoryProtoSerializer


class PublisherService(generics.ModelService):
    queryset = Publisher.objects.all()
    serializer_class = PublisherProtoSerializer


class AuthorService(generics.ModelService):
    queryset = Author.objects.all()
    serializer_class = AuthorProtoSerializer


# class BookService(generics.ModelService):
#     queryset = Book.objects.all()
#     serializer_class = BookProtoSerializer

class BookService(Service):
    def List(self, request, context):
        print("List")
        queryset = Book.objects.all()
        serializer = BookProtoSerializer(queryset, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        ''' 
        self:
        request: book_pb2.Book
        context:
        '''
        print("Create")
        print("request:", request)
        print("request type:", type(request))
        #print("request title", request.get("title"))
        # print("title", request)
        # print("category", request)
        # print("publisher", request)
        # print("author", request)
        serializer = BookProtoSerializer(message=request)
        print("serializer", serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        print("get_object")
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND,
                               'Book:%s not found!' % pk)

    def Retrieve(self, request, context):
        print("Retrieve")
        book = self.get_object(request.id)
        serializer = BookProtoSerializer(book)
        return serializer.message

    def Update(self, request, context):
        print("Update")
        book = self.get_object(request.id)
        serializer = BookProtoSerializer(book, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        print("Destroy")
        book = self.get_object(request.id)
        book.delete()
        return empty_pb2.Empty()
