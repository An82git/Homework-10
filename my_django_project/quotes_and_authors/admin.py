from django.contrib import admin

from .models import Tag, Authors, Quotes

# Register your models here.
admin.site.register(Tag)
admin.site.register(Authors)
admin.site.register(Quotes)
