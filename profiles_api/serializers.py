from rest_framework import serializers

#to validate input data

class HelloSerializer(serializers.Serializer):
    "serializes a name field for testing our APIView"
    name = serializers.CharField(max_length=10)
