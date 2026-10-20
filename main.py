from faker import Faker

gen = Faker("en_US")


def read_amount():
    while True:
        text = input("How many profiles? ").strip()
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("Enter a number greater than 0.")


def new_person():
    return {
        "Name": f"{gen.first_name()} {gen.last_name()}",
        "Email": gen.email(),
        "Phone": gen.numerify("###-###-####"),
        "City": gen.city(),
    }


amount = read_amount()

for i in range(1, amount + 1):
    person = new_person()
    print(f"\n--- User {i} ---")
    for key, val in person.items():
        print(f"{key}: {val}")