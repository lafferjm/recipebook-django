def categories(request):
    from .models import Category

    categories = []
    if request.user.is_authenticated:
        categories = Category.objects.filter(owner=request.user, subcategory=None)

    return {'categories': categories}
