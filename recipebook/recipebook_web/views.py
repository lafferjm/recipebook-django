from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category, Recipe


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user, category__name=self.kwargs['category'])


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    context_object_name = "recipe"


@login_required
def index(request):
    category_count = Category.objects.filter(owner=request.user).count()
    recipe_count = Recipe.objects.filter(owner=request.user).count()

    return render(request, 'recipebook_web/index.html', {
        "category_count": category_count, 
        "recipe_count": recipe_count})
