from rest_framework import serializers
from .models import user, CustomUser
from django.contrib.auth import authenticate

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['firstName', 'lastName', 'email', 'password']

    def create(self, validated_data):
        client = CustomUser(
            firstName=validated_data.get('firstName', 'default_first_name'),
            lastName=validated_data.get('lastName', 'default_last_name'),
            email=validated_data['email'], 
            password = validated_data['password']           
        )        
        client.save()
        return client
    

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['email', 'password']
        
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")
        return data