from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.home, name='home'),
    path('publications/',views.publications,name='publications'),
     path("query/", views.query_view, name="query"),
    # path('contact/',views.contact,name='contact'),
     path('contact/', contact_view, name='contact'), 
    path('authors/', views.all_authors, name='all_authors'),
    # path('upload/', views.upload_paper, name='upload_paper'),
    # path('paper/<int:paper_id>/', views.paper_detail, name='paper_detail'),
    # path('search/', views.search_papers, name='search_papers'),
]