# ViewSet are used to group similar views based on action inside a class this prevents
# from code repeatation specially for urls path or conf

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shared.serializers.user_serializer import UserSerializer


class UserViewSets(viewsets.ViewSet):

    def get_queryset(self):
        return User.objects.all()

    def list(self, request): 
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # action decorator provide functionality for
    # adding new views
    # detail = False means will act as list method above defined
    # detail = True will pass id as slug in request
    # methods = list of allowed methods
    # url_path = costomize url path ( other wise function name is url path)
    # url_name = contomize the url name (otherwise it will be basename + {function_name})

    @action(detail=False,
            methods=["post", "get"],
            url_path="no_su",
            url_name="no_superuser_users")
    def get_normal_users(self, request):
        queryset = self.get_queryset().filter(is_superuser=False)
        return Response(UserSerializer(queryset, many=True).data)


# Model View Set providers abstraction over the above code by binding this to model


class UserModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = UserSerializer

    queryset = User.objects.all()
