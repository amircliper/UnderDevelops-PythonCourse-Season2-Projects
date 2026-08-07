# یک پیام خوش‌آمدگویی نمایش می‌دهیم تا کاربر بداند وارد چه برنامه‌ای شده است.
print("=" * 50)
print("Be mashin hesab hooshmand UnderDevelops khosh amadid")
print("=" * 50)

# عدد اول را به‌صورت متن از کاربر دریافت می‌کنیم و سپس آن را به عدد اعشاری تبدیل می‌کنیم.
first_number = float(input("Adad aval ra vared konid: "))

# عملگر موردنظر را از کاربر دریافت می‌کنیم.
operator = input("Amalgar ra vared konid (+, -, *, /): ").strip()

# عدد دوم را به‌صورت متن از کاربر دریافت می‌کنیم و سپس آن را به عدد اعشاری تبدیل می‌کنیم.
second_number = float(input("Adad dovom ra vared konid: "))

# مقدار اولیه نتیجه را None قرار می‌دهیم؛ یعنی هنوز هیچ نتیجه‌ای محاسبه نشده است.
result = None

# براساس عملگری که کاربر وارد کرده است، عملیات مناسب را انتخاب می‌کنیم.
match operator:
    # اگر عملگر جمع بود، دو عدد را با هم جمع می‌کنیم.
    case "+":
        result = first_number + second_number

    # اگر عملگر تفریق بود، عدد دوم را از عدد اول کم می‌کنیم.
    case "-":
        result = first_number - second_number

    # اگر عملگر ضرب بود، دو عدد را در هم ضرب می‌کنیم.
    case "*":
        result = first_number * second_number

    # اگر عملگر تقسیم بود، ابتدا بررسی می‌کنیم عدد دوم صفر نباشد.
    case "/":
        # تقسیم بر صفر در ریاضی تعریف نشده است؛ بنابراین قبل از تقسیم آن را کنترل می‌کنیم.
        if second_number == 0:
            print("Khata: Taghsim bar sefr emkanpazir nist.")
        else:
            result = first_number / second_number

    # اگر هیچ‌کدام از عملگرهای معتبر وارد نشده بود، پیام مناسب نمایش می‌دهیم.
    case _:
        print("Khata: Amalgar vared shode motabar nist.")

# فقط زمانی نتیجه را نمایش می‌دهیم که یک محاسبه موفق انجام شده باشد.
if result is not None:
    print(f"Natije mohasebe: {first_number} {operator} {second_number} = {result}")

# در پایان اجرای برنامه یک پیام خداحافظی نمایش می‌دهیم.
print("Barname be payan resid.")