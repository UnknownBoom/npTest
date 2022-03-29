import uuid

from django.forms import model_to_dict
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework import views
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from cats.models import User
from cats.permisions import IsOwner
from cats.serializers import UserSerializer


def page_not_found_handler(request, exception):
    return HttpResponse("<h1> Not found</h1>")


class UserApiView(APIView):
    def get(self, request):
        users = User.objects.all().values()
        print(users)
        return Response(list(users))

    def post(self, request):
        user = User.objects.create(
            id=uuid.uuid4(),
            username=request.data['username'],
            password=request.data['password'],
        )
        return Response(model_to_dict(user))


class ModelUserApiView(views.APIView):
    def get(self, request):
        users = User.objects.all().values()
        return UserSerializer(users, many=True)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data


class CatCreateApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserApiUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner,)
    pagination_class = UserPagination

    # def list(self, request, *args, **kwargs):
    #     print("Get list")
    #     # data: QuerySet = User.objects.all().order_by('-id')[:1]
    #     # print(data)
    #     # data = {
    #     #     'id' : uuid.uuid4(),
    #     #     'username' : f'qwerty123{uuid.uuid4()}',
    #     #     'password' : f'{uuid.uuid4()}',
    #     # }
    #     data = request.data
    #     serializer: ModelSerializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.data)
