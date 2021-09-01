from django.urls import path
from .views import (HomePageView, MessageView, UserProfile, delete_message,
                    spam_message, AddReview, AbouUs, ContactUs, ReviewView, SettingsView, EditProfile)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/', UserProfile.as_view(), name='user_profile'),
    # path('profile/edit/<int:pk>', EditProfile.as_view(), name='edit_profile'),
    path('profile/edit/<str:username>', EditProfile, name='edit_profile'),
    path('about/', AbouUs.as_view(), name='about'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('review/', ReviewView, name='review'),
    path('review/add/', AddReview, name='add_review'),
    path('settings/', SettingsView, name='settings'),
    path('message/<str:username>', MessageView, name='message'),
    path('delete/<int:m_id>/', delete_message, name='delete'),
    path('spam/<int:user_id>/', spam_message, name='spam'),
]
