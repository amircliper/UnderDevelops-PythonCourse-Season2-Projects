# ماژول math ابزارهای محاسباتی آماده مانند جذر را در اختیار ما قرار می‌دهد.
import math


# تابع جمع دو عدد را تعریف می‌کنیم.
def add(first_number, second_number):
    """دو عدد را با هم جمع می‌کند."""

    # حاصل جمع را برمی‌گردانیم.
    return first_number + second_number


# تابع تفریق دو عدد را تعریف می‌کنیم.
def subtract(first_number, second_number):
    """عدد دوم را از عدد اول کم می‌کند."""

    # حاصل تفریق را برمی‌گردانیم.
    return first_number - second_number


# تابع ضرب دو عدد را تعریف می‌کنیم.
def multiply(first_number, second_number):
    """دو عدد را در هم ضرب می‌کند."""

    # حاصل ضرب را برمی‌گردانیم.
    return first_number * second_number


# تابع تقسیم دو عدد را تعریف می‌کنیم.
def divide(first_number, second_number):
    """عدد اول را بر عدد دوم تقسیم می‌کند."""

    # تقسیم بر صفر را کنترل می‌کنیم.
    if second_number == 0:
        # برای وضعیت نامعتبر یک خطای قابل مدیریت ایجاد می‌کنیم.
        raise ZeroDivisionError("taghsim bar sefr emkanpazir nist.")

    # حاصل تقسیم را برمی‌گردانیم.
    return first_number / second_number


# تابع توان را تعریف می‌کنیم.
def power(base_number, exponent_number):
    """عدد اول را به توان عدد دوم می‌رساند."""

    # عملگر ** برای محاسبه توان استفاده می‌شود.
    return base_number ** exponent_number


# تابع باقیمانده تقسیم را تعریف می‌کنیم.
def remainder(first_number, second_number):
    """باقیمانده تقسیم عدد اول بر عدد دوم را برمی‌گرداند."""

    # محاسبه باقیمانده نیز با عدد دوم صفر امکان‌پذیر نیست.
    if second_number == 0:
        # یک خطای مشخص ایجاد می‌کنیم.
        raise ZeroDivisionError("mohasebe baghimande ba adad dovom sefr emkanpazir nist.")

    # عملگر درصد باقیمانده تقسیم را محاسبه می‌کند.
    return first_number % second_number


# تابع تقسیم صحیح را تعریف می‌کنیم.
def floor_divide(first_number, second_number):
    """خارج‌قسمت صحیح تقسیم عدد اول بر عدد دوم را برمی‌گرداند."""

    # پیش از تقسیم، صفر نبودن عدد دوم را بررسی می‌کنیم.
    if second_number == 0:
        # خطای تقسیم بر صفر ایجاد می‌کنیم.
        raise ZeroDivisionError("taghsim sahih bar sefr emkanpazir nist.")

    # عملگر // تقسیم صحیح را انجام می‌دهد.
    return first_number // second_number


# تابع جذر را تعریف می‌کنیم.
def square_root(number):
    """جذر یک عدد نامنفی را محاسبه می‌کند."""

    # در مجموعه اعداد حقیقی، جذر عدد منفی تعریف نشده است.
    if number < 0:
        # یک خطای ValueError با پیام قابل فهم ایجاد می‌کنیم.
        raise ValueError("baraye mohasebe jazr bayad adad sefr ya mosbat vared shavad.")

    # از تابع sqrt موجود در ماژول math استفاده می‌کنیم.
    return math.sqrt(number)


# تابع قدر مطلق را تعریف می‌کنیم.
def absolute_value(number):
    """فاصله عدد از صفر را بدون توجه به علامت آن برمی‌گرداند."""

    # تابع داخلی abs قدر مطلق را محاسبه می‌کند.
    return abs(number)


# تابع فاکتوریل را به‌صورت بازگشتی پیاده‌سازی می‌کنیم.
def factorial_recursive(number):
    """فاکتوریل یک عدد صحیح نامنفی را با روش بازگشتی محاسبه می‌کند."""

    # برای جلوگیری از عبور از محدودیت عمق بازگشت پایتون، عددهای بسیار بزرگ را نمی‌پذیریم.
    if number > 900:
        # پیام خطای قابل فهم ایجاد می‌کنیم.
        raise ValueError("baraye noskhe bazgashti, adad bayad 900 ya kmtr bashad.")

    # شرط توقف بازگشت را تعریف می‌کنیم؛ فاکتوریل صفر و یک برابر یک است.
    if number in (0, 1):
        # با برگرداندن یک، زنجیره فراخوانی‌های بازگشتی متوقف می‌شود.
        return 1

    # تابع خودش را با عددی یک واحد کوچک‌تر فراخوانی می‌کند.
    return number * factorial_recursive(number - 1)


# یک عدد اعشاری معتبر از کاربر دریافت می‌کنیم.
def get_number(message):
    """تا زمان دریافت عدد معتبر، ورودی گرفتن را ادامه می‌دهد."""

    # حلقه دریافت ورودی را تکرار می‌کنیم.
    while True:
        # تبدیل متن به عدد ممکن است خطا ایجاد کند.
        try:
            # ورودی را به float تبدیل می‌کنیم.
            return float(input(message))

        # خطای تبدیل ورودی را مدیریت می‌کنیم.
        except ValueError:
            # پیام راهنما نمایش می‌دهیم.
            print("khata: lotfan yek adad motabar vared konid.")


# یک عدد صحیح نامنفی دریافت می‌کنیم.
def get_non_negative_integer(message):
    """فقط عدد صحیح صفر یا مثبت را از کاربر می‌پذیرد."""

    # دریافت ورودی تا رسیدن به مقدار معتبر ادامه دارد.
    while True:
        # تبدیل متن به int ممکن است خطا ایجاد کند.
        try:
            # ورودی را به عدد صحیح تبدیل می‌کنیم.
            number = int(input(message))

            # اگر عدد منفی بود، اجازه ادامه نمی‌دهیم.
            if number < 0:
                # خطای ValueError ایجاد می‌کنیم تا در همین تابع مدیریت شود.
                raise ValueError

            # عدد صحیح نامنفی را برمی‌گردانیم.
            return number

        # هر ورودی غیرصحیح یا منفی در این بخش مدیریت می‌شود.
        except ValueError:
            # نمونه ورودی معتبر را به کاربر نشان می‌دهیم.
            print("khata: lotfan yek adad sahih sefr ya mosbat manand 0, 4 ya 12 vared konid.")


# یک انتخاب معتبر از منو دریافت می‌کنیم.
def get_menu_choice(valid_choices):
    """فقط یکی از گزینه‌های مجاز منو را می‌پذیرد."""

    # تا دریافت گزینه معتبر، حلقه ادامه پیدا می‌کند.
    while True:
        # ورودی کاربر را دریافت می‌کنیم.
        choice = input("shomare amaliat murdanazr ra vared konid: ").strip()

        # عضویت گزینه در تاپل معتبرها را بررسی می‌کنیم.
        if choice in valid_choices:
            # گزینه معتبر را برمی‌گردانیم.
            return choice

        # پیام خطا نمایش می‌دهیم.
        print("khata: lotfan yeki az shomarehaye mojud dar meno ra vared konid.")


# منوی کامل عملیات‌ها را نمایش می‌دهیم.
def show_menu():
    """عملیات‌های ساده و پیشرفته ماشین‌حساب را نمایش می‌دهد."""

    # عنوان و گزینه‌های منو را چاپ می‌کنیم.
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
    print("0. khoruj")
    print("=" * 55)


# عملیات‌های دوورودی را اجرا می‌کنیم.
def calculate_binary_operation(choice, first_number, second_number):
    """یکی از عملیات‌هایی را که به دو عدد نیاز دارد اجرا می‌کند."""

    # انتخاب کاربر را به تابع محاسباتی مناسب متصل می‌کنیم.
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


# عملیات‌های تک‌ورودی را اجرا می‌کنیم.
def calculate_unary_operation(choice, number):
    """یکی از عملیات‌هایی را که فقط به یک عدد نیاز دارد اجرا می‌کند."""

    # انتخاب کاربر را بررسی می‌کنیم.
    match choice:
        case "8":
            return square_root(number)
        case "9":
            return absolute_value(number)
        case _:
            return None


# تابع اصلی برنامه را تعریف می‌کنیم.
def main():
    """منوی کامل ماشین‌حساب را اجرا می‌کند."""

    # تمام گزینه‌های قابل قبول را داخل یک تاپل قرار می‌دهیم.
    valid_choices = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

    # شماره عملیات‌های دوورودی را در یک مجموعه قرار می‌دهیم.
    binary_choices = {"1", "2", "3", "4", "5", "6", "7"}

    # شماره عملیات‌های تک‌ورودی را در یک مجموعه قرار می‌دهیم.
    unary_choices = {"8", "9"}

    # برنامه تا انتخاب خروج ادامه پیدا می‌کند.
    while True:
        # منو را نمایش می‌دهیم.
        show_menu()

        # انتخاب معتبر را دریافت می‌کنیم.
        choice = get_menu_choice(valid_choices)

        # گزینه خروج را بررسی می‌کنیم.
        if choice == "0":
            # پیام خداحافظی نمایش می‌دهیم.
            print("az hamrahi shoma moteshakkerim. khodahafez!")

            # حلقه اصلی را متوقف می‌کنیم.
            break

        # عملیات را در یک بلوک try اجرا می‌کنیم تا خطاهای قابل پیش‌بینی مدیریت شوند.
        try:
            # اگر انتخاب جزو عملیات‌های دوورودی بود، دو عدد دریافت می‌کنیم.
            if choice in binary_choices:
                # عدد اول را دریافت می‌کنیم.
                first_number = get_number("adad aval ra vared konid: ")

                # عدد دوم را دریافت می‌کنیم.
                second_number = get_number("adad dovom ra vared konid: ")

                # عملیات دوورودی را انجام می‌دهیم.
                result = calculate_binary_operation(choice, first_number, second_number)

            # اگر انتخاب جزو عملیات‌های تک‌ورودی بود، فقط یک عدد دریافت می‌کنیم.
            elif choice in unary_choices:
                # عدد موردنیاز عملیات را دریافت می‌کنیم.
                number = get_number("adad ra vared konid: ")

                # عملیات تک‌ورودی را انجام می‌دهیم.
                result = calculate_unary_operation(choice, number)

            # گزینه 10 به فاکتوریل اختصاص دارد و ورودی صحیح نامنفی نیاز دارد.
            else:
                # عدد صحیح نامنفی را دریافت می‌کنیم.
                number = get_non_negative_integer("adad sahih sefr ya mosbat ra vared konid: ")

                # فاکتوریل عدد را با تابع بازگشتی محاسبه می‌کنیم.
                result = factorial_recursive(number)

            # نتیجه موفق را نمایش می‌دهیم.
            print(f"natije: {result}")

        # خطاهای تقسیم بر صفر را مدیریت می‌کنیم.
        except ZeroDivisionError as error:
            # پیام خطا را نمایش می‌دهیم.
            print(f"khata: {error}")

        # خطاهای مربوط به مقدار نامعتبر، مانند جذر عدد منفی را مدیریت می‌کنیم.
        except ValueError as error:
            # پیام خطا را نمایش می‌دهیم.
            print(f"khata: {error}")


# بررسی می‌کنیم فایل مستقیماً اجرا شده باشد.
if __name__ == "__main__":
    # تابع اصلی برنامه را اجرا می‌کنیم.
    main()
