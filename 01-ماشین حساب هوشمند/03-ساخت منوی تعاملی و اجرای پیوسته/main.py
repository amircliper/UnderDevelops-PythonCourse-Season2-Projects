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

    # تقسیم بر صفر را پیش از انجام عملیات کنترل می‌کنیم.
    if second_number == 0:
        # پیام خطای مناسب نمایش می‌دهیم.
        print("khata: taghsim bar sefr emkanpazir nist.")

        # مقدار None یعنی نتیجه معتبری تولید نشده است.
        return None

    # حاصل تقسیم را برمی‌گردانیم.
    return first_number / second_number


# منوی اصلی برنامه را نمایش می‌دهیم.
def show_menu():
    """گزینه‌های قابل انتخاب ماشین‌حساب را نمایش می‌دهد."""

    # یک خط جداکننده برای خوانایی بیشتر چاپ می‌کنیم.
    print("\n" + "=" * 50)

    # عنوان منو را نمایش می‌دهیم.
    print("mashinhesab hushmand UnderDevelops")

    # گزینه‌های موجود را به کاربر نشان می‌دهیم.
    print("1. jam")
    print("2. tafrigh")
    print("3. zarb")
    print("4. taghsim")
    print("0. khoruj")

    # خط پایانی منو را نمایش می‌دهیم.
    print("=" * 50)


# براساس شماره انتخاب‌شده، عملیات مناسب را اجرا می‌کنیم.
def calculate_by_choice(choice, first_number, second_number):
    """شماره منو و دو عدد را دریافت می‌کند و نتیجه محاسبه را برمی‌گرداند."""

    # با match انتخاب کاربر را بررسی می‌کنیم.
    match choice:
        # گزینه 1 مربوط به جمع است.
        case "1":
            return add(first_number, second_number)

        # گزینه 2 مربوط به تفریق است.
        case "2":
            return subtract(first_number, second_number)

        # گزینه 3 مربوط به ضرب است.
        case "3":
            return multiply(first_number, second_number)

        # گزینه 4 مربوط به تقسیم است.
        case "4":
            return divide(first_number, second_number)

        # اگر شماره دیگری وارد شود، نتیجه معتبر نداریم.
        case _:
            return None


# تابع اصلی برنامه را تعریف می‌کنیم.
def main():
    """منوی برنامه را تا زمانی که کاربر گزینه خروج را انتخاب کند، اجرا می‌کند."""

    # حلقه بی‌نهایت می‌سازیم تا ماشین‌حساب پس از هر عملیات دوباره آماده استفاده باشد.
    while True:
        # منوی برنامه را نمایش می‌دهیم.
        show_menu()

        # انتخاب کاربر را به‌صورت رشته دریافت می‌کنیم.
        choice = input("shomare amaliat murdanazr ra vared konid: ").strip()

        # اگر کاربر گزینه صفر را انتخاب کرد، از حلقه خارج می‌شویم.
        if choice == "0":
            # پیام خداحافظی نمایش می‌دهیم.
            print("az hamrahi shoma moteshakkerim. khodahafez!")

            # دستور break اجرای حلقه while را متوقف می‌کند.
            break

        # انتخاب‌های معتبر را داخل یک تاپل نگهداری می‌کنیم.
        valid_choices = ("1", "2", "3", "4")

        # اگر انتخاب کاربر در تاپل گزینه‌های معتبر نبود، پیام خطا نمایش می‌دهیم.
        if choice not in valid_choices:
            # کاربر را از اشتباه بودن گزینه مطلع می‌کنیم.
            print("khata: lotfan yeki az shomarehaye mojud dar meno ra vared konid.")

            # با continue به ابتدای حلقه برمی‌گردیم و منو دوباره نمایش داده می‌شود.
            continue

        # عدد اول را از کاربر دریافت می‌کنیم.
        first_number = float(input("adad aval ra vared konid: "))

        # عدد دوم را از کاربر دریافت می‌کنیم.
        second_number = float(input("adad dovom ra vared konid: "))

        # محاسبه موردنظر را انجام می‌دهیم.
        result = calculate_by_choice(choice, first_number, second_number)

        # فقط نتیجه معتبر را نمایش می‌دهیم.
        if result is not None:
            # نتیجه را در یک جمله خوانا چاپ می‌کنیم.
            print(f"natije: {result}")


# بررسی می‌کنیم فایل مستقیماً اجرا شده باشد.
if __name__ == "__main__":
    # تابع اصلی برنامه را اجرا می‌کنیم.
    main()
