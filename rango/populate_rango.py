import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_rango_project.settings')

import django

django.setup()

from rango.models import Category, Page


def populate():

    python_cat = add_cat('Python')
    django_cat = add_cat('Django')
    other_cat = add_cat('Other Frameworks')


    add_page(cat=python_cat, title="Official Python Tutorial", url="https://docs.python.org/3/tutorial/")
    add_page(cat=python_cat, title="Learn Python", url="https://www.learnpython.org/")

    add_page(cat=django_cat, title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/2.2/intro/tutorial01/")
    add_page(cat=django_cat, title="Django Rocks", url="https://www.djangorocks.com/")

    add_page(cat=other_cat, title="Flask Mega Tutorial",
             url="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world")

    print("Database population complete!")


def add_cat(name):
    c, created = Category.objects.get_or_create(name=name)
    c.save()
    return c


def add_page(cat, title, url):
    p, created = Page.objects.get_or_create(category=cat, title=title, url=url)
    p.save()
    return p


if __name__ == '__main__':
    print("Populating Rango database...")
    populate()

