from django import template


register = template.Library()


def previous_page(page):
    if page is None:
        page = 0

    return page - 1 if page > 0 else None


register.filter('previous_page', previous_page)