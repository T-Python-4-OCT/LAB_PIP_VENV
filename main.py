from faker import Faker

def main():
    fake = Faker()
    try:
        count_input = input("How many profiles? ")
        count = int(count_input)
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(1, count + 1):
        print(f"\n--- User {i} ---")
        print(f"Name: {fake.name()}")
        print(f"Email: {fake.email()}")
        print(f"Phone: {fake.phone_number()}")
        print(f"City: {fake.city()}")

if __name__ == "__main__":
    main()
