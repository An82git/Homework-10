from django.core.paginator import Paginator, EmptyPage
from django import template

from quotes_and_authors.forms import Quotes


register = template.Library()


def page(page):
    page = page if page else 1
    quotes_objects = Quotes.objects.all()
    paginator = Paginator(quotes_objects, 10)
    try:
        quotes = paginator.page(page)
    except EmptyPage:
        quotes = []
    return quotes


register.filter('page', page)