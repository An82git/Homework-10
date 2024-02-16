from django.urls import path
from . import views


app_name = 'quotes_and_authors'

urlpatterns = [
    path('', views.main, name='main'),
    path('page/<int:page>/', views.page, name='page'),
    path('author/create/', views.create_author, name='create_author'),
    path('quote/create/', views.create_quote, name='create_quote'),
    path('author/<str:author_name>/', views.author, name='author'),
    path('sort/tag/<str:tag>/', views.sort_tag, name='sort_tag'),
    path('test/', views.test, name='test'),
]
