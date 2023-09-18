from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('volunteer/', views.volunteer_form_submit, name='volunteer'),
    path('news-details/<int:news_id>/', views.get_news_details, name='news-details'),
    path('news-list-category/<int:category_id>/', views.get_specific_category, name='news-list'),
    path('news-list-tag/<int:tag_id>/', views.get_specific_tag_item, name='news-list_tag'),
    path('news-letter/', views.NewsLetterView.as_view(), name='news-letter'),
    path('contact-form/', views.ContactView.as_view(), name='contact-form'),
    path('news-list/', views.all_news_list, name='news-list'),
    path('donation/', views.donation_view, name='donation'),
    path('donation/payment/', views.DonationPayment.as_view(), name='donation-payment'),
    path('comment/<int:news_id>/', views.CommentView.as_view(), name='comment'),
    path('search/', views.search_news, name='search_news'),
    # path('search/', views.search, name='search'),

]
