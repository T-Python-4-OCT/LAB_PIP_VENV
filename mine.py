from faker import Faker

fake = Faker()

count = int(input("How many profiles? "))

for i in range(1, count + 1):
    name = fake.name()
    email = name.lower().replace(" ", ".") + "@example.com"
    print(f"\n--- User {i} ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {fake.phone_number()}")
    print(f"City: {fake.city()}")

    #MohammedAlnsafi