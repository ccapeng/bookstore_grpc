# from .models import Category, Publisher, Author, Book
# from django_grpc_framework import generics, proto_serializers
# import demo_pb2
# import demo_pb2_grpc


# class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
#     class Meta:
#         model = User
#         proto_class = demo_pb2.User
#         fields = ['id', 'username', 'email']


# class UserService(generics.ModelService):
#     queryset = User.objects.all()
#     serializer_class = UserProtoSerializer


# urlpatterns = []


# def grpc_handlers(server):
#     demo_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)


from book.handlers import \
    category_grpc_handlers, \
    publisher_grpc_handlers, \
    author_grpc_handlers, \
    book_grpc_handlers

urlpatterns = []


def grpc_handlers(server):
    category_grpc_handlers(server)
    publisher_grpc_handlers(server)
    author_grpc_handlers(server)
    book_grpc_handlers(server)
