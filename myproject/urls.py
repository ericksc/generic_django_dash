from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dashboard_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard_view),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),  # <-- Add this line
    path('accounts/profile/', views.dashboard_view),
]
