from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:category>/recipes', views.RecipeListView.as_view(), name='recipes'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/edit', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]
