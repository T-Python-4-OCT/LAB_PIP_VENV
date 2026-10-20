from faker import Faker

faker = Faker()

number = int(input("How many profiles? "))

for i in range(number):
    print(f"\n--- User {i+1} ---")
    print("Name:", faker.name())
    print("Email:", faker.email())
    print("Phone:", faker.phone_number())
    print("City:", faker.city())




