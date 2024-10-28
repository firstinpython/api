from rest_framework import serializers
from .models import Videos
from django.contrib.auth.models import User

class VideosSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Videos
#
# class Registration(serializers.ModelSerializer):
#     paasword = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields = ['username','password','email']
#
#     def create(self,validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             password = validated_data['password'],
#             email = validated_data.get('email','')
#         )
#         return user