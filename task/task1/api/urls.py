from django.urls import path,include
from api.views import pepolesViewSet,pepoleList,pepoleDetail,pepolesCreateView,pepolesDeleteView,pepolesUpdateView,homepage
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'pepoles', pepolesViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('home/',homepage ,name='home-page'),
    path('pepoleList/',pepoleList.as_view(),name='item-list'),
    path('pepoleDetail/<int:pk>',pepoleDetail.as_view(),name='pepole-detail'),
    path('pepoles/create/', pepolesCreateView.as_view(), name='pepoles-create'),
    path('pepoles/<int:pk>/update/', pepolesUpdateView.as_view(), name='pepoles-update'),
    path('pepoles/<int:pk>/delete/', pepolesDeleteView.as_view(), name='pepoles-delete'),
]