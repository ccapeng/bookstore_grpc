import grpc
from book_proto import category_pb2, category_pb2_grpc


# with grpc.insecure_channel('localhost:50051') as channel:
with grpc.insecure_channel('localhost:8080') as channel:
    stub = category_pb2_grpc.CategoryControllerStub(channel)
    print('----- Create -----')
    response = stub.Create(category_pb2.Category(name='Comic'))
    print(response, end='')
    print('----- List -----')
    for category in stub.List(category_pb2.CategoryListRequest()):
        print(category, end='')
    print('----- Retrieve -----')
    response = stub.Retrieve(
        category_pb2.CategoryRetrieveRequest(id=response.id))
    print(response, end='')
    print('----- Update -----')
    response = stub.Update(category_pb2.Category(id=response.id, name='t2'))
    print(response, end='')
    #print('----- Delete -----')
    # stub.Destroy(post_pb2.Post(id=response.id))
