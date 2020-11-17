from rest_framework import serializers
from .models import Entity

class EntitySerializer(serializers.ModelSerializer): 

    # Returns the human readable values
    origin = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    class Meta:
        model= Entity
        fields = '__all__'
    def get_origin(self,obj):
        return obj.get_origin_display()
    def get_role(self,obj):
        return obj.get_role_display()