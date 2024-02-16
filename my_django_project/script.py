import os
import django
from django.conf import settings
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_project.settings')

django.setup()


from tools.normalize_data import normalize_authors, normalize_quotes
from quotes_and_authors.models import Quotes, Authors, Tag


def main():
    for author in normalize_authors():
        Authors.objects.get_or_create(
            fullname = author["fullname"],
            born_date = author["born_date"],
            born_location = author["born_location"],
            description = author["description"]
        )

    for quote in normalize_quotes():
        tag_list = []

        for tag in quote["tags"]:
            tag, created = Tag.objects.get_or_create(name = tag)
            tag_list.append(tag)
        
        author_dic = quote["author"]

        author = Authors.objects.filter(
            fullname = author_dic["fullname"],
            born_date = author_dic["born_date"],
            born_location = author_dic["born_location"]
        )[0]

        quote_obj = Quotes(author = author, quote = quote["quote"])
        quote_obj.save()
        quote_obj.tags.add(*tag_list)

if __name__ == "__main__":
    main()
