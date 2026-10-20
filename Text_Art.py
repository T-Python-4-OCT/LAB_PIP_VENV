from faker import Faker

fake = Faker()

while True:
    try:
        count = int(input("How many profiles do you want?: "))
        break
    except ValueError:
        print("Please enter a valid number.")

for i in range(1, count + 1):
    print(f"\n--- User {i} ---")
    print(f"Name: {fake.name()}")
    print(f"Email: {fake.email()}")
    print(f"Phone: {fake.phone_number()}")
    print(f"City: {fake.city()}")