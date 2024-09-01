class Tenant:
    def __init__(self, name, contact_info, lease_start_date):
        self.name = name
        self.contact_info = contact_info
        self.lease_start_date = lease_start_date

    def display_info(self):
        print(f"Tenant Name: {self.name}")
        print(f"Contact Information: {self.contact_info}")
        print(f"Lease Start Date: {self.lease_start_date}")

    def update_contact_info(self, new_contact_info):
        self.contact_info = new_contact_info
        print("Contact information updated successfully.")

# Example usage:
tenant = Tenant("Jenny Sean", "jenny.sean@gmail.com", "2024-08-01")
tenant.display_info()
tenant.update_contact_info("jenny.sean@gmail.com")
tenant.display_info()

#2
from datetime import datetime

class Rent:
    def __init__(self, amount, due_date):
        self.amount = amount
        self.due_date = due_date
        self.payment_status = 'overdue' if datetime.now() > due_date else 'unpaid'

    def record_payment(self):
        self.payment_status = 'paid'

    def check_payment_status(self):
        return self.payment_status

# Example usage:
due_date = datetime(2024, 8, 31)
rent = Rent(1000, due_date)

print(f"Payment Status: {rent.check_payment_status()}")  # Output: overdue or unpaid
rent.record_payment()
print(f"Payment Status: {rent.check_payment_status()}")  # Output: paid

#3
class Apartment:
    def __init__(self, number, square_footage, rent):
        self.number = number
        self.square_footage = square_footage
        self.rent = rent

    def display_details(self):
        print(f"Apartment Number: {self.number}")
        print(f"Square Footage: {self.square_footage} sq ft")
        print(f"Rent: ${self.rent} per month")

# Example usage:
apartment1 = Apartment(101, 850, 1200)
apartment1.display_details()

#4
class TenantInformation:
    def __init__(self, tenant_id, current_apartment):
        self.tenant_id = tenant_id
        self.current_apartment = current_apartment
        self.lease_history = []

    def add_tenant(self, tenant_id, current_apartment):
        self.tenant_id = tenant_id
        self.current_apartment = current_apartment
        self.lease_history = []

    def update_lease_history(self, lease_details):
        self.lease_history.append(lease_details)

    def find_tenant_information(self, tenant_id):
        if self.tenant_id == tenant_id:
            return {
                "Tenant ID": self.tenant_id,
                "Current Apartment": self.current_apartment,
                "Lease History": self.lease_history
            }
        else:
            return "Tenant not found"

# Example usage
tenant = TenantInformation(tenant_id=1, current_apartment="Apt 101")
tenant.update_lease_history("Lease 1: 2020-2021")
tenant.update_lease_history("Lease 2: 2021-2022")

print(tenant.find_tenant_information(1))

#5
from datetime import date

class Policy:
    def __init__(self, policy_id, description, effective_date):
        self.policy_id = policy_id
        self.description = description
        self.effective_date = effective_date

    def __str__(self):
        return f"Policy ID: {self.policy_id}, Description: {self.description}, Effective Date: {self.effective_date}"

class PolicyManager:
    def __init__(self):
        self.policies = []

    def add_policy(self, policy):
        self.policies.append(policy)

    def list_policies(self):
        for policy in self.policies:
            print(policy)

    def check_compliance(self, policy_id):
        for policy in self.policies:
            if policy.policy_id == policy_id:
                return True
        return False

# Example usage
policy1 = Policy(1, "No smoking in the building", date(2024, 1, 1))
policy2 = Policy(2, "Wear ID badges at all times", date(2024, 2, 1))

manager = PolicyManager()
manager.add_policy(policy1)
manager.add_policy(policy2)

manager.list_policies()
print(manager.check_compliance(1))  # Output: True
print(manager.check_compliance(3))  # Output: False

#6
from datetime import datetime

class MaintenanceRequest:
    def __init__(self, request_id, description):
        self.request_id = request_id
        self.description = description
        self.status = "Open"
        self.date_reported = datetime.now()

    def update_status(self, new_status):
        self.status = new_status

    @staticmethod
    def list_open_requests(requests):
        return [request for request in requests if request.status == "Open"]

# Example usage:
# Creating a new maintenance request
request1 = MaintenanceRequest(1, "Leaky faucet in the kitchen")
request2 = MaintenanceRequest(2, "Broken window in the living room")

# Updating the status of a request
request1.update_status("In Progress")

# Listing all open requests
all_requests = [request1, request2]
open_requests = MaintenanceRequest.list_open_requests(all_requests)

for req in open_requests:
    print(f"Request ID: {req.request_id}, Description: {req.description}, Status: {req.status}, Date Reported: {req.date_reported}")

#Task
#1 Task
class Tenant:
    def __init__(self, name, apartment_number, rent_due):
        self.name = name
        self.apartment_number = apartment_number
        self.rent_due = rent_due
        self.payments = []
        self.maintenance_requests = []

    def add_payment(self, amount):
        self.payments.append(amount)
        self.rent_due -= amount

    def add_maintenance_request(self, request):
        self.maintenance_requests.append(request)

class Payment:
    def __init__(self, tenant, amount, date):
        self.tenant = tenant
        self.amount = amount
        self.date = date

class MaintenanceRequest:
    def __init__(self, tenant, description, date):
        self.tenant = tenant
        self.description = description
        self.date = date
# Task 2
def list_overdue_tenants(tenants):
    overdue_tenants = [tenant for tenant in tenants if tenant.rent_due > 0]
    return overdue_tenants

#Task 3
# Create tenants
tenant1 = Tenant("Alice", "A101", 1000)
tenant2 = Tenant("Bob", "B202", 500)

# Add tenants to a list
tenants = [tenant1, tenant2]

# Simulate rent payments
tenant1.add_payment(500)
tenant2.add_payment(200)

# Simulate maintenance requests
tenant1.add_maintenance_request("Leaky faucet")
tenant2.add_maintenance_request("Broken window")

# List overdue tenants
overdue_tenants = list_overdue_tenants(tenants)
for tenant in overdue_tenants:
    print(f"Tenant {tenant.name} in apartment {tenant.apartment_number} owes {tenant.rent_due} in rent.")

#Task 4
import unittest

class TestTenantManagementSystem(unittest.TestCase):
    def test_add_payment(self):
        tenant = Tenant("Alice", "A101", 1000)
        tenant.add_payment(500)
        self.assertEqual(tenant.rent_due, 500)

    def test_add_maintenance_request(self):
        tenant = Tenant("Alice", "A101", 1000)
        tenant.add_maintenance_request("Leaky faucet")
        self.assertEqual(len(tenant.maintenance_requests), 1)

    def test_list_overdue_tenants(self):
        tenant1 = Tenant("Alice", "A101", 1000)
        tenant2 = Tenant("Bob", "B202", 0)
        tenants = [tenant1, tenant2]
        overdue_tenants = list_overdue_tenants(tenants)
        self.assertEqual(len(overdue_tenants), 1)
        self.assertEqual(overdue_tenants[0].name, "Alice")

if __name__ == '__main__':
    unittest.main()
# movie.py
class Movie:
    def __init__(self, movie_id, title, genre):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.rating = 0
        self.watched_count = 0

    def __str__(self):
        return f"{self.title} ({self.genre}) - Rating: {self.rating}"

# user.py
class User:
    def __init__(self, user_id, name, email, subscription):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.subscription = subscription
        self.favourites = []
        self.watched_movies = []

    def add_to_favourites(self, movie):
        self.favourites.append(movie)

    def get_recommendations(self):
        # Return the last 3 added movies as recommendations
        return self.favourites[-3:]

    def mark_as_watched(self, movie):
        self.watched_movies.append(movie)
        movie.watched_count += 1

    def rate_movie(self, movie, rating):
        if 1 <= rating <= 5:
            movie.rating = rating

    def get_watched_movies(self):
        return self.watched_movies

# admin.py
class Admin(User):
    def add_movie(self, library, movie):
        library.add_movie(movie)

    def remove_movie(self, library, movie):
        library.remove_movie(movie)

# subscription.py
class Subscription:
    def __init__(self, subscription_id, user_id, start_date, end_date, trial_period):
        self.subscription_id = subscription_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.trial_period = trial_period

# library.py
class Library:
    def __init__(self):
        self.movies = []
        self.users = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def remove_movie(self, movie):
        self.movies.remove(movie)

    def get_movie(self, movie_id):
        for movie in self.movies:
            if movie.movie_id == movie_id:
                return movie
        return None

    def get_all_movies(self):
        return self.movies
# main.py
from movie import Movie
from user import User
from admin import Admin
from subscription import Subscription
from library import Library

# Create a library
library = Library()

# Create some movies
movie1 = Movie(1, "Inception", "Sci-Fi")
movie2 = Movie(2, "The Matrix", "Action")
movie3 = Movie(3, "Interstellar", "Sci-Fi")

# Create a subscription
subscription = Subscription(1, 1, "2024-08-01", "2025-08-01", True)

# Create a user
user = User(1, "John Doe", "john@example.com", subscription)

# Create an admin
admin = Admin(2, "Admin", "admin@example.com", subscription)

# Admin adds movies to the library
admin.add_movie(library, movie1)
admin.add_movie(library, movie2)
admin.add_movie(library, movie3)

# User interacts with the library
user.add_to_favourites(movie1)
user.add_to_favourites(movie2)
user.add_to_favourites(movie3)

print("Recommendations:", [str(movie) for movie in user.get_recommendations()])

user.mark_as_watched(movie1)
user.rate_movie(movie1, 5)

print("Watched Movies:", [str(movie) for movie in user.get_watched_movies()])

