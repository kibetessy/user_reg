from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser, Report
from .forms import RegistrationForm
from .backends import generate_dummy_report


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            user.is_active = False  # Mark user as inactive until password reset
            user.save()

            # Generate password reset link
            reset_link = request.build_absolute_uri(
                reverse("custom_password_reset", args=[user.id])
            )

            # Send reset email
            send_mail(
                "Set Your Password",
                f"Click the link to set your password: {reset_link}",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            # Render confirmation page
            return render(request, "check_email.html")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def custom_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)

        if user:
            if not user.is_active:
                # Inactive user message
                return render(request, "check_email.html")
            login(request, user)
            return redirect("landing_page")
        else:
            return render(request, "login.html", {"error": "Invalid email or password or activate your account"})
    return render(request, "login.html")

def landing_page(request):
    # Generate a dummy report
    generate_dummy_report()

    # Fetch all reports to display
    reports = Report.objects.all().order_by("-created_at")
    return render(request, "landing_page.html", {"reports": reports})


def reset_password(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        new_password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            return render(request, "reset_password.html", {"error": "Passwords do not match."})

        user.password = make_password(new_password)
        user.is_active = True  # Activate the user
        user.save()
        return redirect("login")
    return render(request, "reset_password.html", {"user": user})
