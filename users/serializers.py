from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class UserValidateSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()
	is_active = serializers.BooleanField(default=False)

class UserCreateSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()

	def validate_username(self, username):
		try:
			User.objects.get(username=username)
			raise ValidationError('User Alredy Exists!')
		except User.DoesNotExist:
			return username

class UserConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)			