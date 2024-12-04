from django.contrib import admin
from django.urls import path
from core.views import register, landing_page, reset_password, custom_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register, name='register'),
     path("login/", custom_login, name="login"),
    path("reset-password/<int:user_id>/", reset_password, name="custom_password_reset"),
    path('landing-page/', landing_page, name='landing_page'),
]
