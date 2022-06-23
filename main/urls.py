from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.createnews, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/change', views.NewsChangeView.as_view(), name='news-change'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')
]