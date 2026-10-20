
from faker import Faker

fake = Faker()

number = int(input("How many profiles? "))

for i in range(1, number + 1):
    print(f"\n--- User {i} ---")
    print(f"Name: {fake.name()}")
    print(f"Email: {fake.email()}")
    print(f"Phone: {fake.phone_number()}")
    print(f"City: {fake.city()}")
