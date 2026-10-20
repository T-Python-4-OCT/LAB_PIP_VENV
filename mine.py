from faker import Faker

fake = Faker()

number = int(input("How many profiles? "))

for i in range(number):
    print(f"\n--- User {i + 1} ---")
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    city = fake.city()
    

    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"City: {city}")
