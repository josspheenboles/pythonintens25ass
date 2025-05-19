from django.urls import path
# from django.contrib.auth.views import *
from .views import *
urlpatterns=[
    #register
    path('register/',Signup.as_view()),
    #login View
    path('login/',LoginView.as_view()),
    # path('login/',LoginView.as_view(template_name='registration/login.html')),
    # # Logout view
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    #
    # # Password change views
    # path('password_change/', PasswordChangeView.as_view(
    #     template_name='accounts/password_change_form.html',
    #     success_url='/password_change/done/'
    # ), name='password_change'),
    # path('password_change/done/', PasswordChangeDoneView.as_view(
    #     template_name='accounts/password_change_done.html'
    # ), name='password_change_done'),
    #
    # # Password reset views
    # path('password_reset/', PasswordResetView.as_view(
    #     template_name='accounts/password_reset_form.html',
    #     email_template_name='accounts/password_reset_email.html',
    #     subject_template_name='accounts/password_reset_subject.txt',
    #     success_url='/password_reset/done/'
    # ), name='password_reset'),
    # path('password_reset/done/', PasswordResetDoneView.as_view(
    #     template_name='accounts/password_reset_done.html'
    # ), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #     template_name='accounts/password_reset_confirm.html',
    #     success_url='/reset/done/'
    # ), name='password_reset_confirm'),
    # path('reset/done/', PasswordResetCompleteView.as_view(
    #     template_name='accounts/password_reset_complete.html'
    # ), name='password_reset_complete'),
]
