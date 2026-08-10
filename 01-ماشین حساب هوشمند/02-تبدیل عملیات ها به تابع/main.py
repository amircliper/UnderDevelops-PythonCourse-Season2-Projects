def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    if second_number == 0:
        print("Khata: Taghsim bar sefr emkanpazir nist.")
        return None

    return first_number / second_number

def calculate(first_number, operator, second_number):
    match operator:
        case "+":
            return add(first_number, second_number)

        case "-":
            return subtract(first_number, second_number)

        case "*":
            return multiply(first_number, second_number)

        case "/":
            return divide(first_number, second_number)

        case _:
            print("Khata: Amalgar vared shode motabar nist.")
            return None

def main():
    print("=" * 50)
    print("Be mashin hesab hooshmand UnderDevelops khosh amadid")
    print("=" * 50)

    first_number = float(input("Adad aval ra vared konid: "))

    operator = input("Amalgar ra vared konid (+, -, *, /): ").strip()

    second_number = float(input("Adad dovom ra vared konid: "))

    result = None

    result = calculate(first_number, operator, second_number)

    if result is not None:
        print(f"Natije mohasebe: {first_number} {operator} {second_number} = {result}")

    print("Barname be payan resid.")

if __name__ == "__main__":
    main()