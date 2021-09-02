from django.urls import include,path
from rest_framework import routers, urlpatterns
from django.views.generic import TemplateView
from . import views
from django.conf.urls.static import static
from django.conf import settings

# router = routers.DefaultRouter()
# router.register(r'stock', views.ListStockView)
# app_name = 'store'

urlpatterns = [
    # path('', include(router.urls)),
    path('', TemplateView.as_view(template_name="store/base.html")),
    path('api-auth/', include('rest_framework.urls',
    namespace='rest_framework')),
] 
# urlpatterns += router.urls