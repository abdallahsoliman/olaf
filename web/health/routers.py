from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from health.models import HeartRate
from health.serializers import HeartRateSerializer

class HeartRateRouter(ModelRouter):
    route_name = 'heart-rate'
    serializer_class = HeartRateSerializer
    model = HeartRate

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

route_handler.register(HeartRateRouter)
