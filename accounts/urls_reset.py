# from django.urls import re_path, reverse_lazy
# from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# urlpatterns = [
#     re_path('^$', PasswordResetView(), {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
#     re_path(r'^done/$', PasswordResetDoneView(), name='password_reset_done'),
#     re_path(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView(),
#         {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
#     re_path('^complete/$', PasswordResetCompleteView(), name='password_reset_complete')
# ]

from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView)


urlpatterns = [
    path("reset-password/", PasswordResetView.as_view(), name="password_reset"),
    path("reset-password/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset-password/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset-password/complete/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]