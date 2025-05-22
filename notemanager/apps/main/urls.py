from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="main"
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('password/change/', auth_views.PasswordChangeView.as_view(
        template_name='main-apps/password_change.html',
        success_url='/password/change/done/'
    ), name='password_change'),

    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='main-apps/password_change_done.html'
    ), name='password_change_done'),
]
