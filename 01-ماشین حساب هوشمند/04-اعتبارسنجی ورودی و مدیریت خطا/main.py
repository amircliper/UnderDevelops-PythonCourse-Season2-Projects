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

    # اگر عدد دوم صفر باشد، یک خطای مشخص ایجاد می‌کنیم.
    if second_number == 0:
        # به‌جای ادامه محاسبه، خطای ZeroDivisionError ایجاد می‌کنیم.
        raise ZeroDivisionError("taghsim bar sefr emkanpazir nist.")

    # در حالت معتبر، حاصل تقسیم را برمی‌گردانیم.
    return first_number / second_number


# یک عدد معتبر از کاربر دریافت می‌کنیم.
def get_number(message):
    """تا زمان دریافت عدد معتبر از کاربر سؤال می‌پرسد و سپس عدد را برمی‌گرداند."""

    # حلقه تا زمانی ادامه پیدا می‌کند که کاربر یک عدد معتبر وارد کند.
    while True:
        # کدی که ممکن است خطا ایجاد کند داخل try قرار می‌گیرد.
        try:
            # ورودی کاربر را دریافت و به عدد اعشاری تبدیل می‌کنیم.
            number = float(input(message))

            # اگر تبدیل موفق بود، عدد را برمی‌گردانیم و تابع پایان می‌یابد.
            return number

        # اگر float نتواند متن واردشده را به عدد تبدیل کند، این بخش اجرا می‌شود.
        except ValueError:
            # به‌جای متوقف شدن برنامه، پیام آموزشی نمایش می‌دهیم.
            print("khata: lotfan yek adad motabar vared konid; baraye mesal 12 ya 3.5")


# یک گزینه معتبر از منو دریافت می‌کنیم.
def get_menu_choice(valid_choices):
    """انتخاب کاربر را دریافت می‌کند و فقط گزینه موجود در valid_choices را می‌پذیرد."""

    # تا زمان ورود گزینه معتبر، دریافت ورودی تکرار می‌شود.
    while True:
        # انتخاب کاربر را دریافت و فاصله‌های اضافی را حذف می‌کنیم.
        choice = input("shomare amaliat murdanazr ra vared konid: ").strip()

        # با عملگر in بررسی می‌کنیم انتخاب در مجموعه گزینه‌های معتبر وجود داشته باشد.
        if choice in valid_choices:
            # گزینه معتبر را به تابع فراخواننده برمی‌گردانیم.
            return choice

        # در صورت نامعتبر بودن ورودی، پیام خطا نمایش می‌دهیم.
        print("khata: lotfan yeki az shomarehaye mojud dar meno ra vared konid.")


# منوی اصلی برنامه را نمایش می‌دهیم.
def show_menu():
    """فهرست عملیات‌های ماشین‌حساب را نمایش می‌دهد."""

    # ظاهر منو را با خطوط جداکننده مرتب می‌کنیم.
    print("\n" + "=" * 50)
    print("mashinhesab hushmand UnderDevelops")
    print("1. jam")
    print("2. tafrigh")
    print("3. zarb")
    print("4. taghsim")
    print("0. khoruj")
    print("=" * 50)


# براساس انتخاب کاربر عملیات مناسب را انجام می‌دهیم.
def calculate_by_choice(choice, first_number, second_number):
    """انتخاب منو و دو عدد را دریافت می‌کند و نتیجه را برمی‌گرداند."""

    # انتخاب کاربر را بررسی می‌کنیم.
    match choice:
        # اجرای عملیات جمع.
        case "1":
            return add(first_number, second_number)

        # اجرای عملیات تفریق.
        case "2":
            return subtract(first_number, second_number)

        # اجرای عملیات ضرب.
        case "3":
            return multiply(first_number, second_number)

        # اجرای عملیات تقسیم.
        case "4":
            return divide(first_number, second_number)

        # این حالت در عمل نباید رخ دهد؛ چون ورودی قبلاً اعتبارسنجی شده است.
        case _:
            return None


# تابع اصلی برنامه را تعریف می‌کنیم.
def main():
    """چرخه کامل دریافت انتخاب، دریافت اعداد، محاسبه و نمایش نتیجه را اجرا می‌کند."""

    # گزینه‌های معتبر منو را در یک تاپل ثابت نگهداری می‌کنیم.
    valid_choices = ("0", "1", "2", "3", "4")

    # اجرای برنامه را تا انتخاب گزینه خروج ادامه می‌دهیم.
    while True:
        # منوی عملیات‌ها را نمایش می‌دهیم.
        show_menu()

        # یک انتخاب معتبر از کاربر دریافت می‌کنیم.
        choice = get_menu_choice(valid_choices)

        # اگر کاربر صفر را انتخاب کرد، حلقه را متوقف می‌کنیم.
        if choice == "0":
            # پیام پایانی برنامه را نمایش می‌دهیم.
            print("az hamrahi shoma moteshakkerim. khodahafez!")

            # از حلقه اصلی خارج می‌شویم.
            break

        # عدد اول را به کمک تابع اعتبارسنجی‌شده دریافت می‌کنیم.
        first_number = get_number("adad aval ra vared konid: ")

        # عدد دوم را به کمک تابع اعتبارسنجی‌شده دریافت می‌کنیم.
        second_number = get_number("adad dovom ra vared konid: ")

        # عملیات ممکن است خطای تقسیم بر صفر ایجاد کند؛ بنابراین آن را داخل try اجرا می‌کنیم.
        try:
            # نتیجه عملیات انتخاب‌شده را محاسبه می‌کنیم.
            result = calculate_by_choice(choice, first_number, second_number)

            # نتیجه محاسبه را نمایش می‌دهیم.
            print(f"natije: {result}")

        # خطای تقسیم بر صفر را به‌صورت اختصاصی مدیریت می‌کنیم.
        except ZeroDivisionError as error:
            # متن خطا را بدون متوقف شدن برنامه نمایش می‌دهیم.
            print(f"khata: {error}")


# بررسی می‌کنیم فایل مستقیماً اجرا شده باشد.
if __name__ == "__main__":
    # تابع اصلی را اجرا می‌کنیم.
    main()
