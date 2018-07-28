from django.contrib import admin

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'api/users', views.UserViewSet, base_name="user")
router.register(r'list',views.Migrate)
router.register(r'tokens',views.Tokens)
router.register(r'comments',views.Comments)

urlpatterns = router.urls