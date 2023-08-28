from django.urls import path

from .views import GoodsListView, GoodDetailView, GoodCreateView, GoodsCategoryView, GoodsSubcategoryView


urlpatterns = [
    path("all", GoodsListView.as_view(), name='goods-all'),
    path("category/<slug:category_slug>/", GoodsCategoryView.as_view(), name='goods-category'),
    path("category/<slug:category_slug>/<str:subcategory_slug>/",
         GoodsSubcategoryView.as_view(), name='goods-subcategory'),
    path("detail/<slug:good_slug>/", GoodDetailView.as_view(), name='good-detail'),
    path("create/", GoodCreateView.as_view(), name='good-create'),

]
