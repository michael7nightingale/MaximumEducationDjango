from django.views.generic import ListView

from .models import Good


class GoodsListView(ListView):
    template_name = "goods/goods.html"
    queryset = Good.objects.all()
    context_object_name = "goods"
