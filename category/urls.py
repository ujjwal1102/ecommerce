
from django.urls import path
from . import views
from django.urls import path, include,re_path

urlpatterns = [
    path('my-categories',views.CreateCategoryView.as_view(),name='my_categories'),
    path('my-list-of-categories',views.ListCategoryView.as_view(),name='my_categories_list'),
    path('filter_category_from_database',views.filter_category_from_database,name='filter_category_from_database'),
]