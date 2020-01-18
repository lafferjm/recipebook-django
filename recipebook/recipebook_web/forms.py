from django import forms
from django.db.models import Exists
from .models import Category, Recipe


class CategoryForm(forms.ModelForm):
    subcategory = forms.ModelChoiceField(queryset=None, required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

        self.fields['subcategory'].queryset = Category.objects.filter(owner=self.request.user, subcategory=None)

    class Meta:
        model = Category
        fields = ['name', 'subcategory']


class RecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.filter(owner=self.request.user)

    class Meta:
        model = Recipe
        fields = ['name', 'recipe', 'ingredients', 'found', 'category']
