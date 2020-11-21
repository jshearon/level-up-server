from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user, GameTypesViewSet
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypesViewSet, 'gametype')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
