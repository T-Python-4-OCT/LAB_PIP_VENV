from faker import Faker

fake=Faker("en_US")
try:
    number=int(input("HOW many profiles you want?"))
    
    
    if number <=0:
        print("Please enter positive number!")
    else:
        for i in range(1,1+number):
            print(f"\n___USER{i}__")
            print(f"name:{fake.name()}")
            print(f"email:{fake.email()}")
            print(f"phone:{fake.phone_number()}")
            print(f"city:{fake.city()}")
            
            
except ValueError :
    print("Please Enter Vailed Number!!!!!!!")            