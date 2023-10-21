from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins

# class PostList(APIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    
    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    

# class PostDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer


#     def get(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         post.delete()
#         return Response({"status": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)



class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

# @api_view()
# def post_list(request):
#     return Response({"message": "hello"})

# @api_view()
# def post_detail(request, id):
#     try: 
#         post = Post.objects.get(id=id)
#         print(post.__dict__)
#         serialiser = PostSerializer(post)
#         print(serialiser.data)
#         return Response(serialiser.data)
#     except Post.DoesNotExist:
#         return Response({"message": "Item Not Found"}, status=status.HTTP_404_NOT_FOUND)


# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
# def postList(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

"""@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request, id):
    posts = get_object_or_404(Post, id=id, status=True)
    if request.method == 'GET':
        print(posts.__dict__)
        serialiser = PostSerializer(posts)
        print(serialiser.data)
        return Response(serialiser.data)
    elif request.method == "PUT":
        serialiser = PostSerializer(posts, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        else:
            return Response(serialiser.errors)
        
    elif request.method == "DELETE":
        posts.delete()
        return Response({"detail": "item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)"""

