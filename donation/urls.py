from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('news-list/', views.news_list_view, name='news-list'),
    path('volunteer/', views.volunteer_form_submit, name='volunteer'),

]
