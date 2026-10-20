
from faker import Faker

fake = Faker()

while True:
    
    try:
        porfiles=int(input("How many profiles do you want? "))
        if porfiles > 0:
             break
        print("Enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

for i in range(porfiles):
    print(f"\n---User{i+1}---")
    print(f"Name:{fake.name()}")
    print(f"Email:{fake.email()}")
    print(f"Phone:{fake.phone_number()}")
    print(f"City:{fake.city()}")
    print("--"*30)
   