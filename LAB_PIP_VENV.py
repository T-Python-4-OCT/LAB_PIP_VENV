from faker import Faker

fake = Faker()

while True:
    text = input("How many profiles do you want? ")
    if text.isdigit() and int(text) > 0:
        count = int(text)
        break
    print("Please enter a positive whole number.")

for number in range(1, count + 1):
    first = fake.first_name()
    last = fake.last_name()
    email = f"{first}.{last}@example.com".lower().replace(" ", "").replace("'", "")

    print(f"\n--- User {number} ---")
    print("Name:", first, last)
    print("Email:", email)
    print("Phone:", fake.phone_number())
    print("City:", fake.city())