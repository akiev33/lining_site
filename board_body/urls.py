from django.urls import path
from .views import (PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, StockDetailView, PostListView, StockListView, PostListView1, PostListView2,
                     PostListView3, PostListView4, PostListView5, StockCreateView, StockUpdateView, StockDeleteView, index, company)

urlpatterns = [
    path('', index, name='index'),
    path('', PostDetailView.as_view(), name='index'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),


    path('man_boots/', PostListView.as_view(), name='man_boots'),
    path('girls_boots/', PostListView1.as_view(), name='girls_boots'),
    path('man_clothes/', PostListView2.as_view(), name='man_clothes'),
    path('girls_clothes/', PostListView3.as_view(), name='girls_clothes'),
    path('man_accessories/', PostListView4.as_view(), name='man_accessories'),
    path('girls_accessories/', PostListView5.as_view(), name='girls_accessories'),


    path('stocks/', StockListView.as_view(), name='stocks'),
    path('company_detail/', company, name='company'),
    path('', StockDetailView.as_view(), name='index'),
    path('stock_create/', StockCreateView.as_view(), name='stock_create'),
    path('stock_detail/<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('stock_update/<int:pk>/', StockUpdateView.as_view(), name='stock_update'),
    path('stock_delete/<int:pk>/', StockDeleteView.as_view(), name='stock_delete'),
]