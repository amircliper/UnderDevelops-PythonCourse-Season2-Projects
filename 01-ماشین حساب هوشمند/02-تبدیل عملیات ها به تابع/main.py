# تابع جمع دو عدد را تعریف می‌کنیم تا منطق جمع در یک بخش مستقل قرار بگیرد.
def add(first_number, second_number):
    """دو عدد را دریافت می‌کند و حاصل جمع آن‌ها را برمی‌گرداند."""

    # نتیجه جمع را به محل فراخوانی تابع برمی‌گردانیم.
    return first_number + second_number


# تابع تفریق دو عدد را تعریف می‌کنیم.
def subtract(first_number, second_number):
    """عدد دوم را از عدد اول کم می‌کند و نتیجه را برمی‌گرداند."""

    # نتیجه تفریق را به محل فراخوانی تابع برمی‌گردانیم.
    return first_number - second_number


# تابع ضرب دو عدد را تعریف می‌کنیم.
def multiply(first_number, second_number):
    """دو عدد را در هم ضرب می‌کند و نتیجه را برمی‌گرداند."""

    # نتیجه ضرب را به محل فراخوانی تابع برمی‌گردانیم.
    return first_number * second_number


# تابع تقسیم دو عدد را تعریف می‌کنیم.
def divide(first_number, second_number):
    """عدد اول را بر عدد دوم تقسیم می‌کند؛ اگر عدد دوم صفر باشد None برمی‌گرداند."""

    # قبل از انجام تقسیم بررسی می‌کنیم که مقسوم‌علیه صفر نباشد.
    if second_number == 0:
        # پیام خطای قابل فهم برای کاربر نمایش می‌دهیم.
        print("khata: taghsim bar sefr emkanpazir nist.")

        # مقدار None نشان می‌دهد که عملیات با موفقیت انجام نشده است.
        return None

    # اگر عدد دوم صفر نبود، حاصل تقسیم را برمی‌گردانیم.
    return first_number / second_number


# این تابع براساس عملگر، تابع مناسب را انتخاب و اجرا می‌کند.
def calculate(first_number, operator, second_number):
    """دو عدد و یک عملگر را دریافت می‌کند و نتیجه عملیات را برمی‌گرداند."""

    # براساس عملگر ورودی، یکی از توابع محاسباتی را فراخوانی می‌کنیم.
    match operator:
        # تابع جمع را اجرا می‌کنیم.
        case "+":
            return add(first_number, second_number)

        # تابع تفریق را اجرا می‌کنیم.
        case "-":
            return subtract(first_number, second_number)

        # تابع ضرب را اجرا می‌کنیم.
        case "*":
            return multiply(first_number, second_number)

        # تابع تقسیم را اجرا می‌کنیم.
        case "/":
            return divide(first_number, second_number)

        # برای عملگر نامعتبر پیام خطا نمایش می‌دهیم.
        case _:
            print("khata: amalgar varedshode motabar nist.")

            # در صورت نامعتبر بودن عملگر، نتیجه‌ای نداریم.
            return None


# تابع اصلی برنامه را تعریف می‌کنیم تا جریان اجرای برنامه یک‌جا مدیریت شود.
def main():
    """ورودی‌ها را دریافت می‌کند، محاسبه را انجام می‌دهد و نتیجه را نمایش می‌دهد."""

    # عنوان برنامه را نمایش می‌دهیم.
    print("=" * 50)
    print("mashinhesab hushmand UnderDevelops")
    print("=" * 50)

    # عدد اول را از کاربر دریافت و به float تبدیل می‌کنیم.
    first_number = float(input("adad aval ra vared konid: "))

    # عملگر را دریافت و فاصله‌های ابتدا و انتهای آن را حذف می‌کنیم.
    operator = input("amalgar ra vared konid (+, -, *, /): ").strip()

    # عدد دوم را از کاربر دریافت و به float تبدیل می‌کنیم.
    second_number = float(input("adad dovom ra vared konid: "))

    # تابع calculate را فراخوانی می‌کنیم و نتیجه را در یک متغیر قرار می‌دهیم.
    result = calculate(first_number, operator, second_number)

    # اگر نتیجه None نبود، یعنی عملیات با موفقیت انجام شده است.
    if result is not None:
        # نتیجه نهایی را با قالب‌بندی خوانا نمایش می‌دهیم.
        print(f"natije mohasebe: {first_number} {operator} {second_number} = {result}")


# بررسی می‌کنیم فایل به‌صورت مستقیم اجرا شده باشد، نه اینکه در فایل دیگری import شده باشد.
if __name__ == "__main__":
    # اجرای برنامه را از تابع main آغاز می‌کنیم.
    main()
