from swampdragon.serializers.model_serializer import ModelSerializer

class HeartRateSerializer(ModelSerializer):
    class Meta:
        model = 'health.HeartRate'
        publish_fields = ('value', 'date')
