from faker import Faker

def fakerProfile():
    fake = Faker()
    FakeProfile = int(input(f'\nHow Many Profiles Do You Want To Generate? '))
    
    for i in range (1, FakeProfile+1) :
        print(f'\n--- User {i} ---\n')
        print(f"Name: {fake.name()} \nEmail: {fake.email()} \nPhone Number: {fake.phone_number()} \nCity: {fake.city()}\n")

fakerProfile()