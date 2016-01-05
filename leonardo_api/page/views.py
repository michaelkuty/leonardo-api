
from leonardo.module.web.models.page import Page
from rest_framework import viewsets

from .serializers import PageSerializer


class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
