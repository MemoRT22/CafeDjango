from django.urls import path
from reviews.views import ReviewCreateView, ReviewDeleteView, ReviewDetailView, ReviewUpdateView, ReviewsListView, ReviewCreatePedido,PedidoSuccess
from .import views

review_patterns = ([
    path('', ReviewsListView.as_view(), name="reviews"),
    path('<int:pk>/<slug:recipe_slug>/', ReviewDetailView.as_view(), name="review"),
    path('create/', ReviewCreateView.as_view(), name="create"),
    path('update/<int:pk>', ReviewUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', ReviewDeleteView.as_view(), name="delete"),
    path('pedido/', views.realizar_pedido, name="detalle_pedido"),
    path('create_pedido/', ReviewCreatePedido.as_view(), name="create_pedido"),
    path('success_pedido/', PedidoSuccess.as_view(), name="success_pedido"),
    path('pedido/', views.realizar_pedido, name="detalle_pedido"),
], 'reviews')
