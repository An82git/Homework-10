from django.core.paginator import Paginator, EmptyPage
from django import template

from datetime import date


register = template.Library()


def pars_born_date(born_date):
    pars_date = date.strftime(born_date, '%B %d, %Y')
    return pars_date


register.filter('pars_born_date', pars_born_date)