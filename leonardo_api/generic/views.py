
from django.apps import apps
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer


def get_model_class(class_name):
    app_name, model_name = class_name.split('.')
    return apps.get_model(app_name, model_name)


class GenericViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows {models} to be viewed or edited.
    """

    def get_serializer_class(self):
        '''Get serializer from concrete django model class or
        create generic serializer which is sufficient for most cases:

            class MyModel:

                serializer_class = MyModelSerializer
        '''

        def get_generic_serializer_class(model_class):
            '''Just as last options create generic serializer'''

            class Serializer(ModelSerializer):

                class Meta:
                    model = model_class

            return Serializer

        # merge default serializer with custom
        serializer = getattr(self.model_class, 'serializer_class', None)
        generic_serializer = get_generic_serializer_class(self.model_class)

        if serializer:
            Serializer = type('Serializer',
                              (generic_serializer, serializer), {})
        else:
            return generic_serializer

        return Serializer

    def get_queryset(self):
        return self.model_class.objects.all()

    @property
    def model_class(self):
        '''load and returns model class from class_name parameter'''
        if not hasattr(self, '_model_class'):
            self._model_class = get_model_class(
                self.kwargs['class_name'])
        return self._model_class
