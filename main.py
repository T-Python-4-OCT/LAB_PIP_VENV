from faker import Faker


fake = Faker()


try:
    number_of_profiles = int(input("How many profiles? "))
except ValueError:
    print("Please enter a number.")
    exit()


for i in range(1, number_of_profiles + 1):

    print(f"\n--- User {i} ---")
    print(f"Name: {fake.name()}")
    print(f"Email: {fake.email()}")
    print(f"Phone: {fake.phone_number()}")
    print(f"City: {fake.city()}")