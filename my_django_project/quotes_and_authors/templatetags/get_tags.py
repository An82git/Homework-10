from django import template


register = template.Library()


def get_tags(quote_tags):
    return quote_tags.all()


register.filter('get_tags', get_tags)