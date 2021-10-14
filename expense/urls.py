from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.views.generic import RedirectView

from . import views
from .views import  AddExpenseView, ExpenseListView,ExpenseUpdateView, ExpenseDeleteView, CategoryListView, AddCategoryView, CategoryUpdateView, CategoryDeleteView
urlpatterns = [
    path('', views.index,name="expenses"),
    path('create-expense',AddExpenseView.as_view(),name='add-expense'),

    path('<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense-update'),

    path('<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense-delete'),
    path('list/', ExpenseListView.as_view(),name="expense-list"),

    path('create-category',AddCategoryView.as_view(),name='add-category'),

    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),

    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    path('listcate/', CategoryListView.as_view(),name="category-list"),

    path('search/',views.search, name='search'),
    path('search-cate/',views.search_cate, name='search-cate'),

]
