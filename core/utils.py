from django.core.mail import send_mail
from django.conf import settings

def send_email_with_link(recipient_email, reset_link):
    """
    Sends an email with the reset password link.

    Args:
        recipient_email (str): The recipient's email address.
        reset_link (str): The URL for resetting the password.

    Raises:
        Exception: Propagates any exceptions for the caller to handle.
    """
    try:
        send_mail(
            "Set Your Password",
            f"Click the link to set your password: {reset_link}",
            settings.EMAIL_HOST_USER,
            [recipient_email],
            fail_silently=False,
        )
    except Exception as e:
        # Optionally log the error or re-raise it
        print(f"Failed to send email to {recipient_email}: {e}")
        raise
