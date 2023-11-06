from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.RegistrationView.as_view(), name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.dashboard_view, name="profile"),
    path("transaction/new", views.make_transaction_view, name="make-transaction"),
    path("transaction/previous", views.previous_transaction_view, name="history"),
    path("transaction/token/use/<int:pk>/", views.use_token, name="use-token"),
    path("account/recharge/", views.recharge_account, name="recharge"),
]
