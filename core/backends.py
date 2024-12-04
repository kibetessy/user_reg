from datetime import datetime
import random
from .models import Report

def generate_dummy_report():
    """Function to generate a dummy report."""
    report_items = [
        {"name": "Travel Requests",
            "description": "Generated travel reports for this visit."},
        {"name": "Payslip", "description": "Monthly salary data updated dynamically."},
        {"name": "User Management",
            "description": "User activity statistics updated dynamically."},
    ]
    item = random.choice(report_items)
    report = Report.objects.create(
        title=item["name"],
        content=item["description"],
        status=random.choice(["Success", "Pending", "Failed"]),
        created_at=datetime.now(),
    )
    return report
