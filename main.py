from faker import Faker


fake = Faker()


number = int(input("How many profiles? "))


for i in range(number):
    print(f"\n--- User {i+1}---")
    print("Name:", fake.name())
    print("Email:",fake.email())
    print("Phone:", fake.phone_number())
    print("City:", fake.city())
    print("id",fake.iana_id())
