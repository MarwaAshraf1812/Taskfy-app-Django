from django.contrib.auth.models import User

from rest_framework import serializers #type: ignore


class UserSerializer(serializers.ModelSerializer):
    """
    A serializer class for the User model.
    
    """
    password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(read_only=True)

    def create(self, validated_data):
        """
        Create a new User instance and set the password using the create_user method.

        :param validated_data: The validated data from the request.
        :type validated_data: dict
        :return: The new User instance.
        """
        print("Creating user with data:", validated_data)  # Debug statement
        # remove the password from the validated data and create the user
        password = validated_data.pop('password')
        # create the user
        user = User.objects.create(**validated_data)
        # set the password using this method to ensure it is properly hashed.
        user.set_password(password)
    
        user.save()

        return user
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'password']
