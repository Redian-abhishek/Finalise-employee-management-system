from django.core.management.base import BaseCommand
from emp .models import Emp

class Command(BaseCommand):
    help = 'Delete all Employee data'

    def handle(self, *args, **kwargs):
        # Retrieve all Employee objects
        employees = Emp.objects.all()

        # Delete all Employee objects
        employees.delete()

        # Print a message indicating successful deletion
        self.stdout.write(self.style.SUCCESS('All Employee data has been deleted.'))
