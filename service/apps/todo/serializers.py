from .models import TodoTask
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoTask
        fields = ('id', 'uuid', 'task', 'due', 'done')

