from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic.list import ListView
from .models import Category, Recipe
from .forms import CategoryForm, RecipeForm


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user, category__name=self.kwargs['category'])


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    context_object_name = "recipe"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    model = Recipe
    template_name_suffix = "_create_form"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name_suffix = '_update_form'
    #fields = ['name', 'found', 'recipe', 'ingredients', 'category']

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.object.id})


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe

    def get_success_url(self):
        return reverse('index')


class CategoryCreateView(LoginRequiredMixin, CreateView):
    form_class = CategoryForm
    model = Category
    template_name_suffix = "_create_form"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        category = form.save(commit=False)
        category.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = "category_list"

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    #fields = ['name', 'subcategory']
    template_name_suffix = "_update_form"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('category-list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category

    def get_success_url(self):
        return reverse('category-list')


@login_required
def index(request):
    category_count = Category.objects.filter(owner=request.user).count()
    recipe_count = Recipe.objects.filter(owner=request.user).count()

    return render(request, 'recipebook_web/index.html', {
        "category_count": category_count, 
        "recipe_count": recipe_count})
