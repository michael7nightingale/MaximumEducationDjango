from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import Good, Category, Subcategory
from .forms import GoodCreationForm


class GoodsListView(ListView):
    template_name = "goods/goods_all.html"
    queryset = Good.objects.all()
    context_object_name = "goods"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update({
            "categories": Category.objects.all(),
            "title": "Goods"
        })
        return data


class GoodsCategoryView(ListView):
    template_name = "goods/goods_category.html"
    context_object_name = "goods"

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        self.category = get_object_or_404(Category, slug=category_slug)
        return Good.objects.filter(subcategory__category=self.category)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update({
            "subcategories": Subcategory.objects.filter(category=self.category),
            "title": "Goods"
        })
        return data


class GoodsSubcategoryView(ListView):
    template_name = "goods/goods_subcategory.html"
    context_object_name = "goods"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update({
            "title": "Goods"
        })
        return data

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        subcategory_slug = self.kwargs.get("subcategory_slug")
        self.subcategory = get_object_or_404(Subcategory, slug=subcategory_slug, category__slug=category_slug)
        return Good.objects.filter(subcategory=self.subcategory)


class GoodDetailView(DetailView):
    template_name = "goods/good.html"
    context_object_name = "good"
    slug_field = "slug"
    slug_url_kwarg = "good_slug"

    def get_queryset(self):
        return Good.objects.all()


class GoodCreateView(LoginRequiredMixin, CreateView):
    template_name = "goods/create.html"
    form_class = GoodCreationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect(reverse("good-detail", kwargs={"good_slug": obj.slug}))
        else:
            return redirect(reverse("good-create"))
