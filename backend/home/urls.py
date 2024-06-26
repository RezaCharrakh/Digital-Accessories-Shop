from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('home/', views.HomePageView.as_view(), name="home-page"),
    path('product/<int:pk>/', views.DetailPageView.as_view(), name="detail-page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)