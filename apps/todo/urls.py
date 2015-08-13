from django.conf.urls import url, include
from rest_framework import routers
from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

