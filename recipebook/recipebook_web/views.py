from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Recipe


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template = 'recipebook_web/recipe_list.html'

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user, category__name=self.kwargs['category'])


def index(request):
    return render(request, 'recipebook_web/index.html')
