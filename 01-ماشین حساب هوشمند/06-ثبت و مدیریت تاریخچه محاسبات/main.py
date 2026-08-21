import math
from datetime import datetime

def format_number(number):
    if isinstance(number, float) and number.is_integer():
        return str(int(number))

    if isinstance(number, float):
        return f'{number:.10g}'

    return str(number)

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

def power(base_number, exponent_number):



    return base_number ** exponent_number

def remainder(first_number, second_number):



    if second_number == 0:

        raise ZeroDivisionError("mohasebe baghimande ba adad dovom sefr emkanpazir nist.")


    return first_number % second_number

def floor_divide(first_number, second_number):



    if second_number == 0:

        raise ZeroDivisionError("taghsim sahih bar sefr emkanpazir nist.")


    return first_number // second_number

def square_root(number):
    if number < 0:
        raise ValueError("baraye mohasebe jazr bayad adad sefr ya mosbat vared shavad.")
    return math.sqrt(number)

def absolute_value(number):
    return abs(number)

def factorial_recursive(number):



    if number > 900:

        raise ValueError("baraye noskhe bazgashti, adad bayad 900 ya kmtr bashad.")


    if number in (0, 1):

        return 1


    return number * factorial_recursive(number - 1)

def get_number(message):



    while True:

        try:

            return float(input(message))


        except ValueError:

            print("khata: lotfan yek adad motabar vared konid.")

def get_non_negative_integer(message):



    while True:

        try:

            number = int(input(message))


            if number < 0:

                raise ValueError


            return number


        except ValueError:

            print("khata: lotfan yek adad sahih sefr ya mosbat manand 0, 4 ya 12 vared konid.")

def get_menu_choice(valid_choices):



    while True:

        choice = input("shomare amaliat murdanazr ra vared konid: ").strip()


        if choice in valid_choices:

            return choice


        print("khata: lotfan yeki az shomarehaye mojud dar meno ra vared konid.")

def get_operation_title(choice):
    operation_titles = {
        "1": "jam",
        "2": "tafrigh",
        "3": "zarb",
        "4": "taghsim",
        "5": "tavan",
        "6": "baghimande taghsim",
        "7": "tsghsim sahih",
        "8": "jazr",
        "9": "ghadr motlagh",
        "10": "factorial"
    }

    return operation_titles.get(choice, "amaliyat namoshakhas")

def create_history_record(record_id, operation_title, input_values, result):
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "id": record_id,
        "operation": operation_title,
        "inputs": tuple(input_values),
        "result": result,
        "created_at": created_at
    }

def show_history(history):
    if not history:
        print("tarikhche mohasebat khali ast.")
        return

    print("\n" + "-" * 70)
    print("tarikhche mohasebat")
    print('-' * 70)

    for record in history:
        inputs_text = ", ".join(format_number(value) for value in record["inputs"])

        result_text = format_number(record["result"])

        print(
            f"#{record['id']} | {record['operation']} | "
            f"vorudiha: {inputs_text} | natije: {result_text} | {record['created_at']}"
        )

def clear_history(history, used_operations):
    if not history:
        print("tarikhche az ghabl khali ast")
        return

    confirmation = input("baraye pak kardan tarikhche ebarat bale ro vared konid: ").strip().lower()

    if confirmation == "bale":
        history.clear()

        used_operations.clear()

        print("tarikhche ba movafaghiyat pak shod.")
    else:
        print("pak kardan tarikhche laghv shod.")

def save_to_history(history, used_operations, operation_title, input_values, result):
    record_id = len(history) + 1

    record = create_history_record(record_id, operation_title, input_values, result)
    history.append(record)
    used_operations.add(operation_title)

def show_used_operations(used_operations):
    if not used_operations:
        print("hanuz hich amaliati anjam nashode ast.")
        return

    sorted_operations = sorted(used_operations)

    operration_text = ", ".join(sorted_operations)

    print(f"amaliathaye estefadeshode: {operration_text}")

def show_menu():

    print("\n" + "=" * 55)
    print("mashinhesab hushmand UnderDevelops")
    print("1. jam do adad")
    print("2. tafrigh do adad")
    print("3. zarb do adad")
    print("4. taghsim do adad")
    print("5. tavan")
    print("6. baghimande taghsim")
    print("7. taghsim sahih")
    print("8. jazr")
    print("9. ghadr motlagh")
    print("10. faktoryel bazgashti")
    print("11. namayesh tarikhche")
    print("12. pak kardan tarikhche")
    print("13. namayesh amaliathaye estefadeshode")
    print("0. khoruj")
    print("=" * 55)

def calculate_binary_operation(choice, first_number, second_number):



    match choice:
        case "1":
            return add(first_number, second_number)
        case "2":
            return subtract(first_number, second_number)
        case "3":
            return multiply(first_number, second_number)
        case "4":
            return divide(first_number, second_number)
        case "5":
            return power(first_number, second_number)
        case "6":
            return remainder(first_number, second_number)
        case "7":
            return floor_divide(first_number, second_number)
        case _:
            return None

def calculate_unary_operation(choice, number):



    match choice:
        case "8":
            return square_root(number)
        case "9":
            return absolute_value(number)
        case _:
            return None

def main():

    history = []

    used_opations = set()

    valid_choices = tuple(str(number) for number in range(0, 14))
    binary_choices = {"1", "2", "3", "4", "5", "6", "7"}
    unary_choices = {"8", "9"}
    while True:
        show_menu()
        choice = get_menu_choice(valid_choices)
        if choice == "0":
            print("az hamrahi shoma moteshakkerim. khodahafez!")
            break

        if choice == "11":
            show_history(history)
            continue

        if choice == "12":
            clear_history(history,used_opations)
            continue

        if choice == "13":
            show_used_operations(used_opations)
            continue

        try:
            operations_title = get_operation_title(choice)

            if choice in binary_choices:
                first_number = get_number("adad aval ra vared konid: ")
                second_number = get_number("adad dovom ra vared konid: ")
                input_values = (first_number, second_number)
                result = calculate_binary_operation(choice, first_number, second_number)
            elif choice in unary_choices:
                number = get_number("adad ra vared konid: ")
                input_values = (number,)
                result = calculate_unary_operation(choice, number)
            else:
                number = get_non_negative_integer("adad sahih sefr ya mosbat ra vared konid: ")
                result = factorial_recursive(number)
            print(f"natije: {result}")
            save_to_history(history, used_opations, operations_title, input_values, result)
        except ZeroDivisionError as error:
            print(f"khata: {error}")
        except ValueError as error:
            print(f"khata: {error}")

if __name__ == "__main__":
    main()