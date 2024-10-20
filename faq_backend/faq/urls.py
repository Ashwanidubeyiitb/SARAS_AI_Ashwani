from django.urls import path
from .views import search_faq

urlpatterns = [
    path('search/', search_faq, name='search_faq'),
]
