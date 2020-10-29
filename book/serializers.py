from django_grpc_framework import proto_serializers
from book.models import Category, Publisher, Author, Book
from book_proto import category_pb2, publisher_pb2, author_pb2, book_pb2


class CategoryProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Category
        proto_class = category_pb2.Category
        fields = ['id', 'name']


class PublisherProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Publisher
        proto_class = publisher_pb2.Publisher
        fields = ['id', 'name']


class AuthorProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Author
        proto_class = author_pb2.Author
        fields = ['id', 'last_name', 'first_name']


class BookProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Book
        proto_class = book_pb2.Book
        fields = ['id', 'title', 'category', 'publisher', 'author']
