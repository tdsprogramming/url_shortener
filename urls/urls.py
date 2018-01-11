# django imports
from django.urls import path

# project imports
from .views import UrlCreateView, redirect_view, UrlDetailView

app_name='urls'

urlpatterns=[
    path('', UrlCreateView.as_view(), name='new'),
    path('<str:shortened_url_ending>', redirect_view, name='redirect'),
    path('your-url/<str:shortened_url_ending>', UrlDetailView.as_view(), name='detail'),
    # path('<str:shortened_url_ending>', UrlRedirectView.as_view(), name='new'),
]
