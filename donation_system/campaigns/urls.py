from django.urls import path
from .views import campaign_list, create_campaign, donate

urlpatterns = [
    path('', campaign_list, name='campaign_list'),
    path('create/', create_campaign, name='create_campaign'),
    path('donate/<int:campaign_id>/', donate, name='donate'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('campaigns/', include('campaigns.urls')),
    from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('campaigns/', include('campaigns.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
from django.urls import path
from .views import campaign_list, create_campaign, donate, register

urlpatterns = [
    path('', campaign_list, name='campaign_list'),
    path('create/', create_campaign, name='create_campaign'),
    path('donate/<int:campaign_id>/', donate, name='donate'),
    path('register/', register, name='register'),
]