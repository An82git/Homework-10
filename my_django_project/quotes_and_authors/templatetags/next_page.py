from django.core.paginator import Paginator, EmptyPage
from django import template

from quotes_and_authors.forms import Quotes


register = template.Library()


def next_page(page):
    if page is None:
        page = 2
    quotes_objects = Quotes.objects.all()
    paginator = Paginator(quotes_objects, 10)
    
    try:
        quotes = paginator.page(page)
        page = page + 1 if len(quotes) == 10 else None

    except EmptyPage:
        page = None
    return page


register.filter('next_page', next_page)