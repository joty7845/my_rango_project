from django.shortcuts import render, get_object_or_404
from rango.models import Category, Page

def index(request):
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)

def show_category(request, category_name_slug):
    category = get_object_or_404(Category, slug=category_name_slug)
    pages = Page.objects.filter(category=category)

    context_dict = {
        'category': category,
        'pages': pages
    }
    return render(request, 'rango/category.html', context_dict)





