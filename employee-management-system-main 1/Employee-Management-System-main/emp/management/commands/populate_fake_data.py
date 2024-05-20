from django.core.management.base import BaseCommand
from faker import Faker
from emp.models import Emp

class Command(BaseCommand):
    help = 'Populate Employee model with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        try:
            addresses = set()  # Set to store unique addresses
            departments = set()  # Set to store unique departments

            # Generate a pool of unique addresses
            while len(addresses) < 100:  # Adjust the number as needed
                addresses.add(fake.unique.address())

            # Generate a pool of unique job titles
            while len(departments) < 50:  # Adjust the number as needed
                departments.add(fake.unique.job())

            for _ in range(10):  # Generate 10 fake employees
                phone_number = '9' + str(fake.random_number(digits=9))
                # Generate a 10-digit phone number

                # Select a unique address randomly
                address = fake.random_element(addresses)

                # Select a unique department randomly
                department = fake.random_element(departments)

                emp = Emp(
                    name=fake.name(),
                    phone=phone_number,
                    emp_id=str(fake.random_number(digits=5)),
                    address=address,
                    working=fake.boolean(),
                    department=department,
                )
                emp.save()
                print(f'Creating employee: {emp.name}, {emp.emp_id}, {emp.phone}, {emp.address}, {emp.department}')  # Print employee details
            self.stdout.write(self.style.SUCCESS('Successfully populated Emp model with fake data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
