from rest_framework import serializers

from leonardo.module.web.models.page import Page


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ['title']
