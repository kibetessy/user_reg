import random
from django.core.management.base import BaseCommand
from core.models import Report  # Assuming Report model exists

class Command(BaseCommand):
    help = "Generate dummy reports for dashboard items"

    def handle(self, *args, **kwargs):
        report_items = [
            {"name": "Travel Requests", "description": "Generated travel reports for this month."},
            {"name": "Payslip", "description": "Monthly salary data updated."},
            {"name": "User Management", "description": "User activity statistics generated."},
        ]

        for item in report_items:
            Report.objects.create(
                title=item["name"],
                content=item["description"],
                status=random.choice(["Success", "Pending", "Failed"]),
            )
            self.stdout.write(f"Report generated for {item['name']}")

        self.stdout.write("Dummy reports successfully generated.")
