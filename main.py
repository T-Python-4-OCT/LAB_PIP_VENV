from faker import Faker 
fake = Faker()
count = int(input("How many profiles? "))

for i in range(count):

    print(f"\n--- User {i + 1} ---")

    print("Name:", fake.name())
    print("Email:", fake.email())
    print("Phone:", fake.phone_number())
    print("City:", fake.city())