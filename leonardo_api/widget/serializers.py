from leonardo.module.web.models.widget import WidgetDimension
from rest_framework import serializers


class WidgetDimensionSerializer(serializers.ModelSerializer):

    class Meta:

        model = WidgetDimension


class WidgetDimensionsField(serializers.RelatedField):
    """
    A custom field to use for the `dimensions` generic relationship.
    """

    def to_representation(self, value):
        if isinstance(value, WidgetDimension):
            return WidgetDimensionSerializer(value).data

        raise Exception('Unexpected type of tagged object')


class WidgetSerializer(serializers.Serializer):

    dimensions = WidgetDimensionsField(many=True,
                                       queryset=WidgetDimension.objects.all())
