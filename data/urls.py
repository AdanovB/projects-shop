from django.urls import path
from .views import ProductViewSet, RecommendationsViewSet, CategoryViewSet, OrderViewSet, AddressViewSet


urlpatterns = [
    path('prod-create/', ProductViewSet.as_view({'post': 'create'})),
    path('prod-list/', ProductViewSet.as_view({'get': 'list'})),
    path('prod-change/<int:pk>/', ProductViewSet.as_view({'patch': 'update'})),
    path('prod-detail/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('prod-delete/<int:pk>/', ProductViewSet.as_view({'delete': 'destroy'})),

    path('rec-create/', RecommendationsViewSet.as_view({'post': 'create'})),
    path('rec-list/', RecommendationsViewSet.as_view({'get': 'list'})),
    path('rec-change/<int:pk>/', RecommendationsViewSet.as_view({'patch': 'update'})),
    path('rec-detail/<int:pk>/', RecommendationsViewSet.as_view({'get': 'retrieve'})),
    path('rec-delete/<int:pk>/', RecommendationsViewSet.as_view({'delete': 'destroy'})),

    path('category-create/', CategoryViewSet.as_view({'post': 'create'})),
    path('category-list/', CategoryViewSet.as_view({'get': 'list'})),
    path('category-change/<int:pk>/', CategoryViewSet.as_view({'patch': 'update'})),
    path('category-detail/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('category-delete/<int:pk>/', CategoryViewSet.as_view({'delete': 'destroy'})),

    path('order-create/', OrderViewSet.as_view({'post': 'create'})),
    path('order-list/', OrderViewSet.as_view({'get': 'list'})),
    path('order-change/<int:pk>/', OrderViewSet.as_view({'patch': 'update'})),
    path('order-detail/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve'})),
    path('order-delete/<int:pk>/', OrderViewSet.as_view({'delete': 'destroy'})),

    path('ordering-create/', AddressViewSet.as_view({'post': 'create'})),
    path('ordering-list/', AddressViewSet.as_view({'get': 'list'})),
    path('ordering-change/<int:pk>/', AddressViewSet.as_view({'patch': 'update'})),
    path('ordering-detail/<int:pk>/', AddressViewSet.as_view({'get': 'retrieve'})),
    path('ordering-delete/<int:pk>/', AddressViewSet.as_view({'delete': 'destroy'})),

]
#start