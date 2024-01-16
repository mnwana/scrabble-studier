from rest_framework import serializers
from flashcard_app import models
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework import status

class DictionarySerializer(serializers.ModelSerializer):
  class Meta:
      fields = [
          'id',
          'title',
          'description',
          'file',
          'user',
          'public',
          'words_q1',
          'words_q2',
          'words_q3',
          'words_q4',
          'preview',
      ]
      model = models.Dictionary   
  def create(self, validated_data):
    dictionary = models.Dictionary.objects.create(
      title=validated_data['title'],
      description=validated_data['description'],
      public= validated_data['public'],
      
      file=validated_data['file']
    )
    dictionary.save()
    return dictionary    
        
class UserSerializer(serializers.ModelSerializer):
    dictionaries = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Dictionary.objects.all())
    
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password', 
            'dictionaries'
        ]

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
#   password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 
         'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user