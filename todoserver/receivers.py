from django.dispatch import receiver

from account.signals import password_changed
from account.signals import user_sign_up_attempt, user_signed_up
from account.signals import user_login_attempt, user_logged_in

from eventlog.models import log

@receiver(user_logged_in)
def handle_user_logged_in(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="USER_LOGGED_IN",
        extra={}
    )


@receiver(password_changed)
def handle_password_changed(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="PASSWORD_CHANGED",
        extra={}
    )


@receiver(user_login_attempt)
def handle_user_login_attempt(sender, **kwargs):
    log(
        user=None,
        action="LOGIN_ATTEMPTED",
        extra={
            "username": kwargs.get("username"),
            "result": kwargs.get("result")
        }
    )


@receiver(user_sign_up_attempt)
def handle_user_sign_up_attempt(sender, **kwargs):
    log(
        user=None,
        action="SIGNUP_ATTEMPTED",
        extra={
            "username": kwargs.get("username"),
            "email": kwargs.get("email"),
            "result": kwargs.get("result")
        }
    )


@receiver(user_signed_up)
def handle_user_signed_up(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="USER_SIGNED_UP",
        extra={}
    )

from django.db.models.signals import post_save, post_delete, m2m_changed
from todo.models import TodoTask
from todo.serializers import TodoSerializer
from . import mqtt

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

