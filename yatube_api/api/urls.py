from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views


v1_router = DefaultRouter()

v1_router.register(r'posts', PostViewSet, basename='index')
v1_router.register(r'groups', GroupViewSet, basename='group')
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comment')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]
