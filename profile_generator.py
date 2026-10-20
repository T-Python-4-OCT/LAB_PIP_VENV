from faker import Faker


fake = Faker()


def generate_profile(fake):
    return {
        "name": fake.name(),
        "email": fake.email(),
      "phone": fake.phone_number(),
      "city": fake.city(),

    }



def print_users():
    count = int(input("how many users you want? :"))
    for i in range(count):
        profile = generate_profile(fake)

        print(f"\n--- User {i + 1} ---")
        print(f"Name: {profile['name']}")
        print(f"Email: {profile['email']}")
        print(f"Phone: {profile['phone']}")
        print(f"City: {profile['city']}")

print_users()