from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    subcategory = forms.ModelChoiceField(queryset=None, required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

        self.fields['subcategory'].queryset = Category.objects.filter(owner=self.request.user, subcategory=None)

    class Meta:
        model = Category
        fields = ['name', 'subcategory']
