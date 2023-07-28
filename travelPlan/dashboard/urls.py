from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('', views.index, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('explore/', views.explore, name='explore'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)