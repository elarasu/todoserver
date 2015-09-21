from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import TodoTask
from .serializers import TodoSerializer
from todoserver import mqtt

#{'update_fields': None, 'instance': <TodoTask: 2 a 0>, 'signal': <django.db.models.signals.ModelSignal object at 0x7f7acbdfe4d0>, 'created': False, 'raw': False, 'using': 'default'}
@receiver(post_save, sender=TodoTask)
def my_handler(sender, **kwargs):
    obj = kwargs.get("instance")
    res = {}
    res['id'] = obj.id
    res['data'] = TodoSerializer(obj).data
    if kwargs.get("created"):
        res['event']='add'
    else:
        res['event']='set'
    mqtt.client.publish("/data/todos", res);

#{'instance': <TodoTask: 2 a 0>, 'signal': <django.db.models.signals.ModelSignal object at 0x7f7acbdfe5d0>, 'using': 'default'}
@receiver(post_delete, sender=TodoTask)
def my_delete_handler(sender, **kwargs):
    obj = kwargs.get("instance")
    res = {}
    res['id'] = obj.id
    res['event'] = 'remove'
    mqtt.client.publish("/data/todos", res);
