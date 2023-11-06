from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from . import models, forms
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
class RegistrationView(CreateView):
    form_class = forms.UserCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request, request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            if user is not None and user.is_active:
                login(request, user)
                return redirect("profile")  # Replace with the actual success URL

    else:
        form = forms.LoginForm()

    return render(request, "registration/login.html", {"form": form})


def logout_view(request):
    logout(request)  # Log the user out
    return redirect("home")


def home_view(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        return redirect("register")


@login_required(login_url="login")
def dashboard_view(request):
    user = models.CustomUser.objects.get(id=request.user.id)
    account = models.Account.objects.get(user=user)
    meter = models.Meter.objects.get(user=user)
    Transaction = models.Transaction.objects.filter(account=account)
    context = {
        "username": user.username.title(),
        "account_no": account.account_id,
        "account_balance": account.balance,
        "meter": meter,
        "transactions": Transaction[:5],
    }

    return render(request, "dashboard.html", context)


@login_required(login_url="login")
def make_transaction_view(request):
    form = forms.TransactionForm()
    account = models.Account.objects.get(user=request.user)
    balance = account.balance
    if request.method == "POST":
        form = forms.TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            account = models.Account.objects.get(user=request.user)
            account.balance -= transaction.amount
            transaction.account = account
            account.save()
            transaction.save()
            return redirect("profile")

    return render(
        request, "transaction.html", {"form": form, "account_balance": balance}
    )


@login_required(login_url="login")
def previous_transaction_view(request):
    transactions = models.Transaction.objects.filter(account=request.user.account)

    return render(
        request,
        "history.html",
        {
            "transactions": transactions,
            "username": request.user.username.title(),
        },
    )


@login_required(login_url="login")
def use_token(request, pk):
    token = models.Token.objects.get(token_id=pk)
    if token.used == False:
        token.meter.unit += token.unit
        token.used = True
        token.meter.save()
        token.save()
    return redirect("profile")


@login_required(login_url="login")
def recharge_account(request):
    account = models.Account.objects.get(user=request.user)
    if request.method == "POST":
        amountForm = forms.AccountRechargeForm(request.POST)
        if amountForm.is_valid():
            account.balance += amountForm.cleaned_data["amount"]
            account.save()
            return redirect("profile")
    return render(
        request,
        "recharge.html",
        {
            "form": forms.AccountRechargeForm(),
            "account_no": account.account_id,
            "balance": account.balance,
        },
    )
