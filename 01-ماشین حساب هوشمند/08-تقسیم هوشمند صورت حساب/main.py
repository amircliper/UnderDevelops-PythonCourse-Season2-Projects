import math

from datetime import datetime


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


def format_number(number):

    if isinstance(number, float) and number.is_integer():
        return str(int(number))

    if isinstance(number, float):
        return f"{number:.10g}"

    return str(number)


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
            print("khata: lotfan yek adad sahih sefr ya mosbat vared konid.")


def get_menu_choice(valid_choices):

    while True:
        choice = input("shomare gozine murdanazr ra vared konid: ").strip()

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
        "7": "taghsim sahih",
        "8": "jazr",
        "9": "ghadr motlagh",
        "10": "factorial",
    }

    return operation_titles.get(choice, "amaliyat namoshakhas")


def create_history_record(record_id, operation_title, input_values, result):

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "id": record_id,
        "operation": operation_title,
        "inputs": tuple(input_values),
        "result": result,
        "created_at": created_at,
    }


def save_to_history(history, used_operations, operation_title, input_values, result):

    record_id = len(history) + 1

    record = create_history_record(record_id, operation_title, input_values, result)

    history.append(record)

    used_operations.add(operation_title)


def show_history(history):

    if not history:
        print("tarikhche mohasebat khali ast.")

        return

    print("\n" + "-" * 70)
    print("tarikhche mohasebat")
    print("-" * 70)

    for record in history:
        inputs_text = ", ".join(format_number(value) for value in record["inputs"])

        result_text = format_number(record["result"])

        print(
            f"#{record['id']} | {record['operation']} | "
            f"vorudiha: {inputs_text} | natije: {result_text} | {record['created_at']}"
        )


def clear_history(history, used_operations):

    if not history:
        print("tarikhche az ghabl khali ast.")

        return

    confirmation = input("baraye pak kardan tarikhche ebarat bale ra vared konid: ").strip().lower()

    if confirmation == "bale":
        history.clear()

        used_operations.clear()

        print("tarikhche ba movaffaghiyat pak shod.")
    else:
        print("pak kardan tarikhche laghv shod.")


def show_used_operations(used_operations):

    if not used_operations:
        print("hanuz hich amaliati anjam nashode ast.")

        return

    sorted_operations = sorted(used_operations)

    operations_text = "، ".join(sorted_operations)

    print(f"amaliathaye estefadeshode: {operations_text}")


def generate_numeric_results(history):

    for record in history:
        if isinstance(record["result"], (int, float)):
            yield record["result"]


def calculate_history_statistics(history):

    results_iterator = iter(generate_numeric_results(history))

    try:
        first_result = next(results_iterator)
    except StopIteration:
        return None

    count = 1

    total = first_result

    minimum = first_result

    maximum = first_result

    for result in results_iterator:
        count += 1

        total += result

        minimum = min(minimum, result)

        maximum = max(maximum, result)

    average = total / count

    return {
        "count": count,
        "total": total,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
    }


def show_history_report(history, used_operations):

    statistics = calculate_history_statistics(history)

    if statistics is None:
        print("baraye tahiye gozaresh, ebteda chand mohasebe anjam dahid.")

        return

    print("\n" + "-" * 60)
    print("gozaresh amari tarikhche")
    print("-" * 60)

    print(f"tedad mohasebat: {statistics['count']}")
    print(f"majmu natayej: {format_number(statistics['total'])}")
    print(f"miangin natayej: {format_number(statistics['average'])}")
    print(f"kamtarin natije: {format_number(statistics['minimum'])}")
    print(f"bishtarin natije: {format_number(statistics['maximum'])}")

    show_used_operations(used_operations)


def show_sorted_history(history):

    if not history:
        print("tarikhche mohasebat khali ast.")

        return

    print("1. jadidtarin mohasebat")
    print("2. ghadimitarin mohasebat")
    print("3. natije az kuchak be bozorg")
    print("4. nam amaliat")

    sort_choice = get_menu_choice(("1", "2", "3", "4"))

    match sort_choice:
        case "1":
            sorted_history = sorted(history, key=lambda record: record["created_at"], reverse=True)
        case "2":
            sorted_history = sorted(history, key=lambda record: record["created_at"])
        case "3":
            sorted_history = sorted(history, key=lambda record: record["result"])
        case _:
            sorted_history = sorted(history, key=lambda record: record["operation"])

    show_history(sorted_history)


def browse_history_step_by_step(history):

    if not history:
        print("tarikhche mohasebat khali ast.")

        return

    history_iterator = iter(history)

    while True:
        try:
            record = next(history_iterator)

            inputs_text = ", ".join(format_number(value) for value in record["inputs"])

            print(
                f"#{record['id']} | {record['operation']} | "
                f"vorudiha: {inputs_text} | natije: {format_number(record['result'])}"
            )

            command = input("Enter: record badi | khoruj: payan morur: ").strip().lower()

            if command == "khoruj":
                break

        except StopIteration:
            print("be payan tarikhche residid.")

            break



def get_non_negative_number(message):

    while True:
        number = get_number(message)

        if number >= 0:
            return number

        print("khata: mablagh ya darsad nemitavanad manfi bashad.")


def get_percentage(message):

    while True:
        percentage = get_non_negative_number(message)

        if percentage <= 100:
            return percentage

        print("khata: darsad bayad adadi beyn sefr ta sad bashad.")


def get_positive_integer(message):

    while True:
        try:
            number = int(input(message))

            if number <= 0:
                raise ValueError

            return number

        except ValueError:
            print("khata: lotfan yek adad sahih bozorgtar az sefr vared konid.")


def collect_extra_costs():

    extra_costs = []

    print("hazinehaye janebi manand ersal ya servis ra vared konid. baraye payan, Enter bezanid.")

    while True:
        raw_value = input("hazine janebi: ").strip()

        if raw_value == "":
            break

        try:
            extra_cost = float(raw_value)

            if extra_cost < 0:
                raise ValueError

            extra_costs.append(extra_cost)

        except ValueError:
            print("khata: hazine janebi bayad yek adad sefr ya mosbat bashad.")

    return extra_costs


def calculate_final_bill(base_amount, *extra_costs, **rates):

    if base_amount < 0:
        raise ValueError("mablagh paye nemitavanad manfi bashad.")

    if any(extra_cost < 0 for extra_cost in extra_costs):
        raise ValueError("hazinehaye janebi nmy tvannd manfi bashnd.")

    if any(rate < 0 or rate > 100 for rate in rates.values()):
        raise ValueError("drsdha bayad beyn sefr ta sad bashnd.")

    extra_costs_total = sum(extra_costs)

    subtotal = base_amount + extra_costs_total

    discount_percent = rates.get("discount_percent", 0)

    tax_percent = rates.get("tax_percent", 0)

    tip_percent = rates.get("tip_percent", 0)

    discount_amount = subtotal * discount_percent / 100

    discounted_subtotal = subtotal - discount_amount

    tax_amount = discounted_subtotal * tax_percent / 100

    tip_amount = discounted_subtotal * tip_percent / 100

    final_total = discounted_subtotal + tax_amount + tip_amount

    return {
        "base_amount": base_amount,
        "extra_costs_total": extra_costs_total,
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "tax_amount": tax_amount,
        "tip_amount": tip_amount,
        "final_total": final_total,
    }


def run_bill_splitter(history, used_operations):

    print("\n" + "-" * 60)
    print("taghsim hushmand surathesab")
    print("-" * 60)

    base_amount = get_non_negative_number("mablagh paye surathesab: ")

    extra_costs = collect_extra_costs()

    discount_percent = get_percentage("darsad takhfif: ")

    tax_percent = get_percentage("darsad malyat: ")

    tip_percent = get_percentage("darsad anaam: ")

    people_count = get_positive_integer("tedad afrad: ")

    rates = {
        "discount_percent": discount_percent,
        "tax_percent": tax_percent,
        "tip_percent": tip_percent,
    }

    bill_details = calculate_final_bill(base_amount, *extra_costs, **rates)

    per_person_amount = bill_details["final_total"] / people_count

    print("\njoziyat surathesab")
    print(f"mablagh paye: {format_number(bill_details['base_amount'])}")
    print(f"jam hazinehaye janebi: {format_number(bill_details['extra_costs_total'])}")
    print(f"jam avvaliye: {format_number(bill_details['subtotal'])}")
    print(f"mablagh takhfif: {format_number(bill_details['discount_amount'])}")
    print(f"mablagh maliat: {format_number(bill_details['tax_amount'])}")
    print(f"mablagh anam: {format_number(bill_details['tip_amount'])}")
    print(f"mablagh nahai: {format_number(bill_details['final_total'])}")
    print(f"sahm har nafar: {format_number(per_person_amount)}")

    history_inputs = (base_amount, people_count, discount_percent, tax_percent, tip_percent)

    save_to_history(
        history,
        used_operations,
        "taghsim surathesab",
        history_inputs,
        per_person_amount,
    )


def show_menu():

    print("\n" + "=" * 60)
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
    print("14. gozaresh amari tarikhche")
    print("15. namayesh tarikhche morattabshode")
    print("16. morur marhalei tarikhche")
    print("17. taghsim hushmand surathesab")
    print("0. khoruj")
    print("=" * 60)


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

    used_operations = set()

    valid_choices = tuple(str(number) for number in range(0, 18))

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
            clear_history(history, used_operations)

            continue

        if choice == "13":
            show_used_operations(used_operations)

            continue

        if choice == "14":
            show_history_report(history, used_operations)

            continue

        if choice == "15":
            show_sorted_history(history)

            continue

        if choice == "16":
            browse_history_step_by_step(history)

            continue

        if choice == "17":
            run_bill_splitter(history, used_operations)

            continue

        try:
            operation_title = get_operation_title(choice)

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

                input_values = (number,)

                result = factorial_recursive(number)

            print(f"natije: {format_number(result)}")

            save_to_history(history, used_operations, operation_title, input_values, result)

        except ZeroDivisionError as error:
            print(f"khata: {error}")

        except ValueError as error:
            print(f"khata: {error}")


if __name__ == "__main__":
    main()
