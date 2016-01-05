from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    def get_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    def get_date(self, obj):
        return obj.date_joined

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name',
                  'password', 'name', 'date']

# add to User
User.serializer_class = UserSerializer
