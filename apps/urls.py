from django.urls import path

from apps.views import ProductListCreateAPIView

urlpatterns = [
	path('', ProductListCreateAPIView.as_view())
]
