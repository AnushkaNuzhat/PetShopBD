from django.urls import path
from user import views
app_name = 'user_app'


urlpatterns = [
    path('sign_up/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
]
