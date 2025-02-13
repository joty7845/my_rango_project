from django.shortcuts import render
from rango.models import Category

def index(request):
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)


