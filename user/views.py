from django.http import HttpResponseRedirect
from django.conf import settings
from dj_rest_auth.views import LoginView


class UserLoginView(LoginView):
    
    def login(self):
        super().login()

        self.user.refreshToken = self.refresh_token


def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    )


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )
