from rest_framework import serializers
from .import models

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tasks
        fields=('user','title','memo','important','created')

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Basket
        fields = ('id', 'quantity', 'task', 'created_timestamp')
        read_only_fields=('created_timestamp',)






