from datetime import datetime

from .models import Quotes, Authors
from .connect import connect_mongo

connect_mongo()


def normalize_authors():
    for author in Authors.objects.all():
        fullname = author.fullname

        born_date = author.born_date
        date_object = datetime.strptime(born_date,'%B %d, %Y')
        formatted_date = date_object.strftime('%Y-%m-%d')

        born_location = author.born_location
        description = author.description

        yield {"fullname": fullname,
               "born_date": formatted_date,
               "born_location": born_location,
               "description": description}


def normalize_quotes():
    for quote in Quotes.objects.all():
        tags = quote.tags
        quote_data = quote.quote
        author = quote.author

        born_date = author.born_date
        date_object = datetime.strptime(born_date,'%B %d, %Y')
        formatted_date = date_object.strftime('%Y-%m-%d')
        
        yield {"tags": tags,
               "author": {"fullname": author.fullname,
                          "born_date": formatted_date,
                          "born_location": author.born_location
                          },
               "quote": quote_data}
