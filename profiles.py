from faker import Faker

MAX_PROFILES = 100


def ask_count():
    while True:
        text = input("How many profiles? ").strip()
        if text.isascii() and text.isdigit() and int(text) > 0:
            count = int(text)
            if count <= MAX_PROFILES:
                return count
            print(f"Please choose {MAX_PROFILES} profiles or fewer.")
        else:
            print("Please enter a whole number greater than 0.")


def main():
    fake = Faker()
    count = ask_count()

    for number in range(1, count + 1):
        print(f"\n--- User {number} ---")
        print(f"Name: {fake.first_name()} {fake.last_name()}")
        print(f"Email: {fake.email()}")
        print(f"Phone: {fake.phone_number()}")
        print(f"City: {fake.city()}")


if __name__ == "__main__":
    main()