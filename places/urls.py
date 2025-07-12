from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'types', views.TypeViewSet)
router.register(r'ubications', views.UbicationViewSet)
router.register(r'places', views.PlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('type/create/', views.TypeCreateView.as_view(), 
        name='type_create'),
    path('type/count/', views.type_count, 
        name='type_count'),
    path('place/priorityFilter/', views.place_by_priority, 
        name='place_priority'),
]