from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.contrib import admin
from django.urls import path, include
from category.views import CategoryViewSet
from company.views import CompanyViewSet
from sub_category.views import SubCategoryViewSet
from cpu.views import CPUViewSet
from product.views import ProductViewSet


router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'sub-category', SubCategoryViewSet)
router.register(r'cpu', CPUViewSet)
router.register(r'product', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('', include('category.urls'), name='category'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(
        url_name='schema'), name='docs'),
]
