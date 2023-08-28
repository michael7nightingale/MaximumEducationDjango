from django.urls import path, include

from .views import GoodsListView


urlpatterns = [
    path("", GoodsListView.as_view(), name='goods'),

]
