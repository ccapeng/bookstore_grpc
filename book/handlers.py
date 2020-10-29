from book.services import CategoryService, PublisherService, AuthorService, BookService
from book_proto import category_pb2_grpc, publisher_pb2_grpc, author_pb2_grpc, book_pb2_grpc


def category_grpc_handlers(server):
    print("category_grpc_handlers", server)
    category_pb2_grpc.add_CategoryControllerServicer_to_server(
        CategoryService.as_servicer(), server)


def publisher_grpc_handlers(server):
    publisher_pb2_grpc.add_PublisherControllerServicer_to_server(
        PublisherService.as_servicer(), server)


def author_grpc_handlers(server):
    author_pb2_grpc.add_AuthorControllerServicer_to_server(
        AuthorService.as_servicer(), server)


def book_grpc_handlers(server):
    book_pb2_grpc.add_BookControllerServicer_to_server(
        BookService.as_servicer(), server)
