from django.forms import ModelForm, CharField, TextInput, DateInput, DateField
from .models import Tag, Quotes, Authors


class AuthorForm(ModelForm):

    fullname = CharField(max_length=20, required=True, widget=TextInput())
    born_date = DateField(required=True, widget=DateInput())
    born_location = CharField(max_length=50, required=True, widget=TextInput())
    description = CharField(required=False, widget=TextInput())

    class Meta:
        model = Authors
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(ModelForm):
    
    quote = CharField(required=True, widget=TextInput())

    class Meta:
        model = Quotes
        fields = ['quote', 'author']
        exclude = ['tags']
