from rest_framework.routers import SimpleRouter
from category.views import CategoryViewSet

router = SimpleRouter()
router.register(r'category', CategoryViewSet)
urlpatterns = router.urls
