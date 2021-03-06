from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework_simplejwt import views as jwt_views

from api.chat import views


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()
rooms_router = router.register('rooms', views.RoomViewSet)
rooms_router.register(
    'messages',
    views.MessageViewSet,
    base_name='room-messages',
    parents_query_lookups=['room']
)


urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.CreateUserView.as_view()),
    path('users/<int:pk>/', views.DetailUserView.as_view()),
    path('auth/login', jwt_views.TokenObtainPairView.as_view()),
    path('auth/refresh', jwt_views.TokenRefreshView.as_view()),
]
