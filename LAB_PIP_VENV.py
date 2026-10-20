"""Generate and print realistic fake user profiles in the terminal."""

from faker import Faker


def main() -> None:
    fake = Faker()

    try:
        profile_count = int(input("How many profiles? "))
        if profile_count < 0:
            raise ValueError
    except ValueError:
        print("Please enter a non-negative whole number.")
        return

    for user_number in range(1, profile_count + 1):
        print(f"\n--- User {user_number} ---")
        print(f"Name: {fake.name()}")
        print(f"Email: {fake.email()}")
        print(f"Phone: {fake.phone_number()}")
        print(f"City: {fake.city()}")


if __name__ == "__main__":
    main()
