def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        raise ZeroDivisionError("taghsim bar sefr emkanpazir nist.")

    return first_number / second_number

def get_number(message):

    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("khata: lotfan yek adad motabar vared konid; baraye mesal 12 ya 3.5")

def show_menu():
    print("\n" + "=" * 50)

    print("mashinhesab hushmand UnderDevelops")

    print("1. jam")
    print("2. tafrigh")
    print("3. zarb")
    print("4. taghsim")
    print("0. khoruj")

    print("=" * 50)


def calculate_by_choice(choice, first_number, second_number):

    match choice:
        case "1":
            return add(first_number, second_number)

        case "2":
            return subtract(first_number, second_number)

        case "3":
            return multiply(first_number, second_number)

        case "4":
            return divide(first_number, second_number)

        case _:
            return None


def main():
    """منوی برنامه را تا زمانی که کاربر گزینه خروج را انتخاب کند، اجرا می‌کند."""

    while True:
        show_menu()

        choice = input("shomare amaliat murdanazr ra vared konid: ").strip()

        if choice == "0":
            print("az hamrahi shoma moteshakkerim. khodahafez!")

            break

        valid_choices = ("1", "2", "3", "4")

        if choice not in valid_choices:
            print("khata: lotfan yeki az shomarehaye mojud dar meno ra vared konid.")

            continue

        first_number = get_number("adad aval ra vared konid: ")

        second_number = get_number("adad dovom ra vared konid: ")

        try:
            result = calculate_by_choice(choice, first_number, second_number)
            print(f"natije: {result}")

        except ZeroDivisionError as error:
            print(f"khata: {error}")


if __name__ == "__main__":
    main()
