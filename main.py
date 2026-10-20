
from faker import Faker

fake = Faker()

print("=" * 35)
print("      FAKE PROFILE GENERATOR")
print("=" * 35)

number = int(input("How many profiles? "))

for i in range(number):
    print(f"--- User {i + 1} ---")
    print(f"Name: {fake.name()}")
    print(f"Email: {fake.email()}")
    print(f"Phone: {fake.numerify(text="05########")}")
    print(f"City: {fake.city()}")

    print("-" * 35)

