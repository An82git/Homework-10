from django.db.models import Count
from django import template

from quotes_and_authors.forms import Tag


register = template.Library()


def top_tags(count_tags):
    return Tag.objects.annotate(quote_count=Count('quotes')).order_by('-quote_count')[:count_tags]


register.filter('top_tags', top_tags)