from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('goods/', include("goods.urls")),
    path('', include("home.urls")),

]
