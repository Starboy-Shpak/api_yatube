from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views


router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='index')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
