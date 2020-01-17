from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:category>/recipes', views.RecipeListView.as_view(), name='recipes'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('category/', views.CategoryCreateView.as_view(), name='category-create')
]
