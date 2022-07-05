
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from auto.models import Auto
from auto.permissions import IsAdminOrReadOnly
from auto.serializers import AutoSerializer


class AutoAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class AutoAPIList(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = AutoAPIListPagination


class AutoAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsAuthenticated,)


class AutoAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsAdminOrReadOnly,)


