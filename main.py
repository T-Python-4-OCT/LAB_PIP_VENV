from faker import Faker

fake = Faker()


def ask_profile_count():
    while True:
        answer = input("How many profiles? ").strip()
        if answer.isdigit() and int(answer) > 0:
            return int(answer)
        print("Please enter a positive whole number.")


def generate_profile():
    return {
        "Name": fake.name(),
        "Email": fake.email(),
        "Phone": fake.phone_number(),
        "City": fake.city(),
    }


def display_profile(number, profile):
    print(f"\n--- User {number} ---")
    for field, value in profile.items():
        print(f"{field}: {value}")


def main():
    count = ask_profile_count()
    for number in range(1, count + 1):
        display_profile(number, generate_profile())


if __name__ == "__main__":
    main()
