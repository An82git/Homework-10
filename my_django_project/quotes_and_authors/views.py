from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from .forms import AuthorForm, QuoteForm
from .models import Authors, Tag, Quotes


count_tags = 10


# Create your views here.
def test(request):

    return render(request, 'quotes_and_authors/test.html')

def main(request):
    page = 1
    return render(request, 'quotes_and_authors/index.html', {'page': page, 'count_tags': count_tags})

def page(request, page = 1):
    return render(request, 'quotes_and_authors/index.html', {'page': page, 'count_tags': count_tags})

def author(request, author_name):
    author = get_object_or_404(Authors, fullname=author_name)
    return render(request, 'quotes_and_authors/author.html', {'author': author})

def sort_tag(request, tag):
    quotes = get_list_or_404(Quotes, tags__name=tag)
    return render(request, 'quotes_and_authors/sort_tags.html', {'quotes': quotes, 'count_tags': count_tags})

@login_required
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes_and_authors:main')
        else:
            return render(request, 'quotes_and_authors/create_author.html', {'form': form})

    return render(request, 'quotes_and_authors/create_author.html', {'form': AuthorForm()})

@login_required
def create_quote(request):
    tags = Tag.objects.all()
    authors = Authors.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()
            
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to='quotes_and_authors:main')
        else:
            return render(request, 'quotes_and_authors/create_quote.html', {"tags": tags, "authors": authors, 'form': form})

    return render(request, 'quotes_and_authors/create_quote.html', {"tags": tags, "authors": authors, 'form': QuoteForm()})
