from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.decorators import authentication_classes, permission_classes

from api.user.models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        for (k, v) in validated_data.items():
            if k == 'password':
                instance.set_password(v)
            else:
                setattr(instance, k, v)

        instance.save()
        return instance

    class Meta:
        model = User
        extra_kwargs = {'password': {
            'write_only': True
        }}
        fields = ('name',
                  'email',
                  'password',
                  'phone',
                  'gender',
                  'is_active',
                  'is_staff',
                  'is_superuser')
