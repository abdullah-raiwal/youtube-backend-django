from django.urls import path, include
from .views import (UserLoginView,
    email_confirm_redirect, password_reset_confirm_redirect)
from dj_rest_auth.views import (LogoutView, UserDetailsView, LoginView)

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.registration.views import (
    ResendEmailVerificationView, VerifyEmailView)

from dj_rest_auth.views import (PasswordResetConfirmView, PasswordResetView)


urlpatterns = [
    # -------------------------------accounts registration and verifications ---------------------------
    path('register/', RegisterView.as_view(), name='create'),

    path("register/verify-email/", VerifyEmailView.as_view(),
         name="rest_verify_email"),

    path("register/resend-email/", ResendEmailVerificationView.as_view(),
         name="rest_resend_email"),

    path("account-confirm-email/<str:key>/",
         email_confirm_redirect, name="account_confirm_email"),

    path("account-confirm-email/", VerifyEmailView.as_view(),
         name="account_email_verification_sent"),
    # ----------------------------------- password reset verification --------------------------------

    path("password/reset/", PasswordResetView.as_view(),
         name="rest_password_reset"),

    path("password/reset/confirm/<str:uidb64>/<str:token>/", password_reset_confirm_redirect,
         name="password_reset_confirm",
         ),

    path("password/reset/confirm/", PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    path('auth/login/', UserLoginView.as_view(), name='login-user'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/details/', UserDetailsView.as_view(), name='user-details'),
]
