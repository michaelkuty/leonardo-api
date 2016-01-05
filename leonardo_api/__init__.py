
from django.apps import AppConfig

from .widget import *

default_app_config = 'leonardo_api.Config'


LEONARDO_APPS = [
    'leonardo_api',
    'rest_framework',
    'rest_framework.authtoken'
]
LEONARDO_PUBLIC = True


class Config(AppConfig):
    name = 'leonardo_api'
    verbose_name = "leonardo-api"

    def ready(self):

        from leonardo.module.web.models.page import Page
        from leonardo.module.web.models.widget import Widget
        from leonardo_api.page.serializers import PageSerializer
        from leonardo_api.widget.serializers import WidgetSerializer
        Page.serializer_class = PageSerializer
        Widget.serializer_class = WidgetSerializer

        from .generic.views import GenericViewSet
        from .router import router
        router.register(
            r'models/(?P<class_name>[\w\.\-]+)',
            GenericViewSet, base_name='generic')
