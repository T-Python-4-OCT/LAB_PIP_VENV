from faker import Faker


def main():
    fake = Faker()

    while True:
        try:
            count = int(input("How many profiles? "))
            if count <= 0:
                print("Please enter a positive whole number")
                continue
            break
        except ValueError:
            print("Please enter a positive whole number")

    for number in range(1, count + 1):
        print(f"\n--- User {number} ---")
        print(f"Name: {fake.name()}")
        print(f"Email: {fake.email()}")
        print(f"Phone: {fake.phone_number()}")
        print(f"City: {fake.city()}")


if __name__ == "__main__":
    main()
