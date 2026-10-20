
from faker import Faker

fake = Faker()

try:
    count = int(input("How many profiles? "))

    if count <= 0:
        print("Please enter a positive number.")

    else:
        for i in range(1, count + 1):
            print(f"\n--- User {i} ---")
            print(f"Name: {fake.name()}")
            print(f"Email: {fake.email()}")
            print(f"Phone: {fake.phone_number()}")
            print(f"City: {fake.city()}")

except ValueError:
    print("Invalid input! Please enter a number.")
