from django.conf.urls import url
from . import views

app_name = 'website2'
urlpatterns = [
    # ex: /website/
    url(r'^$', views.latest_books, name='index'),
    # ex: /website/detail/
   
    ]
