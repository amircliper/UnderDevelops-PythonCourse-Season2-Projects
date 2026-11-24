# ماژول math ابزارهای محاسباتی آماده مانند جذر را در اختیار ما قرار می‌دهد.
import math

# کلاس datetime برای ثبت زمان انجام هر محاسبه استفاده می‌شود.
from datetime import datetime


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
        # یک خطای مشخص ایجاد می‌کنیم تا در جریان اصلی مدیریت شود.
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

    # عدد دوم نباید صفر باشد.
    if second_number == 0:
        # خطای قابل مدیریت ایجاد می‌کنیم.
        raise ZeroDivisionError("mohasebe baghimande ba adad dovom sefr emkanpazir nist.")

    # باقیمانده را برمی‌گردانیم.
    return first_number % second_number


# تابع تقسیم صحیح را تعریف می‌کنیم.
def floor_divide(first_number, second_number):
    """خارج‌قسمت صحیح تقسیم عدد اول بر عدد دوم را برمی‌گرداند."""

    # عدد دوم نباید صفر باشد.
    if second_number == 0:
        # خطای تقسیم بر صفر ایجاد می‌کنیم.
        raise ZeroDivisionError("taghsim sahih bar sefr emkanpazir nist.")

    # حاصل تقسیم صحیح را برمی‌گردانیم.
    return first_number // second_number


# تابع جذر را تعریف می‌کنیم.
def square_root(number):
    """جذر یک عدد نامنفی را محاسبه می‌کند."""

    # در اعداد حقیقی، جذر عدد منفی تعریف نشده است.
    if number < 0:
        # یک خطای مقدار نامعتبر ایجاد می‌کنیم.
        raise ValueError("baraye mohasebe jazr bayad adad sefr ya mosbat vared shavad.")

    # جذر را با تابع sqrt محاسبه می‌کنیم.
    return math.sqrt(number)


# تابع قدر مطلق را تعریف می‌کنیم.
def absolute_value(number):
    """قدر مطلق عدد را برمی‌گرداند."""

    # تابع داخلی abs علامت منفی را حذف می‌کند.
    return abs(number)


# تابع فاکتوریل را به‌صورت بازگشتی تعریف می‌کنیم.
def factorial_recursive(number):
    """فاکتوریل عدد صحیح نامنفی را با روش بازگشتی محاسبه می‌کند."""

    # برای جلوگیری از عبور از محدودیت عمق بازگشت پایتون، عددهای بسیار بزرگ را نمی‌پذیریم.
    if number > 900:
        # پیام خطای قابل فهم ایجاد می‌کنیم.
        raise ValueError("baraye noskhe bazgashti, adad bayad 900 ya kmtr bashad.")

    # شرط توقف بازگشت را تعریف می‌کنیم.
    if number in (0, 1):
        # فاکتوریل صفر و یک برابر یک است.
        return 1

    # تابع خودش را با عدد کوچک‌تر فراخوانی می‌کند.
    return number * factorial_recursive(number - 1)


# عدد را برای نمایش زیباتر قالب‌بندی می‌کنیم.
def format_number(number):
    """اگر عدد اعشاری بخش کسری نداشته باشد، آن را بدون .0 نمایش می‌دهد."""

    # بررسی می‌کنیم مقدار از نوع float باشد و قسمت اعشاری آن صفر باشد.
    if isinstance(number, float) and number.is_integer():
        # عدد را به int تبدیل و سپس به رشته تبدیل می‌کنیم.
        return str(int(number))

    # در سایر حالت‌ها عدد را با حداکثر ده رقم معنادار نمایش می‌دهیم.
    if isinstance(number, float):
        # قالب g صفرهای اضافه انتهای عدد اعشاری را حذف می‌کند.
        return f"{number:.10g}"

    # برای اعداد صحیح یا انواع دیگر، تبدیل مستقیم به رشته کافی است.
    return str(number)


# یک عدد معتبر از کاربر دریافت می‌کنیم.
def get_number(message):
    """تا زمان دریافت عدد معتبر، ورودی گرفتن را تکرار می‌کند."""

    # حلقه دریافت ورودی را اجرا می‌کنیم.
    while True:
        # تبدیل ورودی به float ممکن است خطا ایجاد کند.
        try:
            # عدد معتبر را برمی‌گردانیم.
            return float(input(message))

        # خطای تبدیل متن به عدد را مدیریت می‌کنیم.
        except ValueError:
            # پیام راهنما نمایش می‌دهیم.
            print("khata: lotfan yek adad motabar vared konid.")


# یک عدد صحیح نامنفی دریافت می‌کنیم.
def get_non_negative_integer(message):
    """فقط عدد صحیح صفر یا مثبت را می‌پذیرد."""

    # دریافت ورودی را تا رسیدن به مقدار معتبر ادامه می‌دهیم.
    while True:
        # تبدیل متن به عدد صحیح را امتحان می‌کنیم.
        try:
            # ورودی را به int تبدیل می‌کنیم.
            number = int(input(message))

            # اگر عدد منفی بود، آن را نامعتبر می‌دانیم.
            if number < 0:
                # یک خطای ValueError ایجاد می‌کنیم.
                raise ValueError

            # مقدار معتبر را برمی‌گردانیم.
            return number

        # ورودی غیرصحیح یا منفی را مدیریت می‌کنیم.
        except ValueError:
            # پیام راهنما نمایش می‌دهیم.
            print("khata: lotfan yek adad sahih sefr ya mosbat vared konid.")


# یک گزینه معتبر از منو دریافت می‌کنیم.
def get_menu_choice(valid_choices):
    """فقط یکی از گزینه‌های مجاز منو را می‌پذیرد."""

    # دریافت انتخاب را تا ورود گزینه معتبر ادامه می‌دهیم.
    while True:
        # انتخاب کاربر را دریافت می‌کنیم.
        choice = input("shomare gozine murdanazr ra vared konid: ").strip()

        # عضویت انتخاب در گزینه‌های معتبر را بررسی می‌کنیم.
        if choice in valid_choices:
            # انتخاب معتبر را برمی‌گردانیم.
            return choice

        # پیام خطای ورودی نامعتبر را نمایش می‌دهیم.
        print("khata: lotfan yeki az shomarehaye mojud dar meno ra vared konid.")


# عنوان فارسی هر عملیات را برمی‌گردانیم.
def get_operation_title(choice):
    """شماره عملیات را به عنوان فارسی آن تبدیل می‌کند."""

    # یک دیکشنری برای ارتباط شماره منو با عنوان عملیات می‌سازیم.
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

    # عنوان متناظر را برمی‌گردانیم؛ اگر پیدا نشد عبارت نامشخص برمی‌گردد.
    return operation_titles.get(choice, "amaliyat namoshakhas")


# یک رکورد استاندارد برای تاریخچه می‌سازیم.
def create_history_record(record_id, operation_title, input_values, result):
    """اطلاعات یک محاسبه را داخل دیکشنری قرار می‌دهد."""

    # زمان فعلی سیستم را با قالب خوانا ذخیره می‌کنیم.
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # دیکشنری رکورد را می‌سازیم و برمی‌گردانیم.
    return {
        "id": record_id,
        "operation": operation_title,
        "inputs": tuple(input_values),
        "result": result,
        "created_at": created_at,
    }


# یک محاسبه موفق را در تاریخچه ذخیره می‌کنیم.
def save_to_history(history, used_operations, operation_title, input_values, result):
    """رکورد محاسبه را به لیست تاریخچه و نام عملیات را به مجموعه اضافه می‌کند."""

    # شناسه رکورد جدید را براساس تعداد رکوردهای فعلی ایجاد می‌کنیم.
    record_id = len(history) + 1

    # رکورد استاندارد تاریخچه را می‌سازیم.
    record = create_history_record(record_id, operation_title, input_values, result)

    # رکورد جدید را به انتهای لیست تاریخچه اضافه می‌کنیم.
    history.append(record)

    # نام عملیات را به مجموعه عملیات‌های استفاده‌شده اضافه می‌کنیم.
    used_operations.add(operation_title)


# همه رکوردهای تاریخچه را نمایش می‌دهیم.
def show_history(history):
    """محاسبات ثبت‌شده را به‌ترتیب انجام شدن نمایش می‌دهد."""

    # اگر لیست خالی بود، پیام مناسب نمایش می‌دهیم.
    if not history:
        # کاربر را از خالی بودن تاریخچه مطلع می‌کنیم.
        print("tarikhche mohasebat khali ast.")

        # اجرای تابع را متوقف می‌کنیم.
        return

    # عنوان بخش تاریخچه را نمایش می‌دهیم.
    print("\n" + "-" * 70)
    print("tarikhche mohasebat")
    print("-" * 70)

    # روی تمام رکوردهای لیست حرکت می‌کنیم.
    for record in history:
        # ورودی‌های هر رکورد را به رشته‌ای خوانا تبدیل می‌کنیم.
        inputs_text = ", ".join(format_number(value) for value in record["inputs"])

        # نتیجه را قالب‌بندی می‌کنیم.
        result_text = format_number(record["result"])

        # اطلاعات کامل رکورد را نمایش می‌دهیم.
        print(
            f"#{record['id']} | {record['operation']} | "
            f"vorudiha: {inputs_text} | natije: {result_text} | {record['created_at']}"
        )


# تاریخچه و مجموعه عملیات‌ها را پاک می‌کنیم.
def clear_history(history, used_operations):
    """همه محاسبات ثبت‌شده را پس از تأیید کاربر حذف می‌کند."""

    # اگر تاریخچه از قبل خالی بود، نیازی به حذف وجود ندارد.
    if not history:
        # پیام مناسب نمایش می‌دهیم.
        print("tarikhche az ghabl khali ast.")

        # اجرای تابع را پایان می‌دهیم.
        return

    # برای جلوگیری از حذف ناخواسته، از کاربر تأیید می‌گیریم.
    confirmation = input("baraye pak kardan tarikhche ebarat bale ra vared konid: ").strip().lower()

    # فقط با دریافت پاسخ بله، عملیات پاک‌سازی انجام می‌شود.
    if confirmation == "bale":
        # تمام اعضای لیست تاریخچه را حذف می‌کنیم.
        history.clear()

        # تمام اعضای مجموعه عملیات‌ها را نیز حذف می‌کنیم.
        used_operations.clear()

        # موفقیت عملیات را اعلام می‌کنیم.
        print("tarikhche ba movaffaghiyat pak shod.")
    else:
        # لغو عملیات حذف را اعلام می‌کنیم.
        print("pak kardan tarikhche laghv shod.")


# عملیات‌هایی را که حداقل یک بار استفاده شده‌اند نمایش می‌دهیم.
def show_used_operations(used_operations):
    """نام عملیات‌های استفاده‌شده را بدون تکرار نمایش می‌دهد."""

    # اگر مجموعه خالی بود، هنوز عملیاتی ثبت نشده است.
    if not used_operations:
        # پیام مناسب نمایش می‌دهیم.
        print("hanuz hich amaliati anjam nashode ast.")

        # اجرای تابع را متوقف می‌کنیم.
        return

    # اعضای مجموعه را برای نمایش منظم مرتب می‌کنیم.
    sorted_operations = sorted(used_operations)

    # عملیات‌ها را با جداکننده ویرگول به هم متصل می‌کنیم.
    operations_text = "، ".join(sorted_operations)

    # نتیجه را نمایش می‌دهیم.
    print(f"amaliathaye estefadeshode: {operations_text}")


# نتایج عددی تاریخچه را یکی‌یکی تولید می‌کنیم.
def generate_numeric_results(history):
    """نتیجه‌های عددی را با generator و بدون ساختن لیست جدید تولید می‌کند."""

    # روی تمام رکوردهای تاریخچه حرکت می‌کنیم.
    for record in history:
        # فقط نتیجه‌هایی را که عدد هستند در خروجی generator قرار می‌دهیم.
        if isinstance(record["result"], (int, float)):
            # yield مقدار را تحویل می‌دهد و وضعیت تابع را برای ادامه حفظ می‌کند.
            yield record["result"]


# آمار کلی تاریخچه را محاسبه می‌کنیم.
def calculate_history_statistics(history):
    """تعداد، مجموع، میانگین، کمترین و بیشترین نتیجه را محاسبه می‌کند."""

    # از generator یک iterator می‌سازیم.
    results_iterator = iter(generate_numeric_results(history))

    # تلاش می‌کنیم اولین نتیجه را با next دریافت کنیم.
    try:
        # اولین مقدار برای مقداردهی اولیه متغیرهای آماری استفاده می‌شود.
        first_result = next(results_iterator)
    except StopIteration:
        # اگر generator هیچ مقداری نداشت، آمار قابل محاسبه نیست.
        return None

    # تعداد نتایج را با یک مقدار اولیه می‌کنیم.
    count = 1

    # مجموع اولیه برابر اولین نتیجه است.
    total = first_result

    # کمترین مقدار اولیه را برابر اولین نتیجه قرار می‌دهیم.
    minimum = first_result

    # بیشترین مقدار اولیه را برابر اولین نتیجه قرار می‌دهیم.
    maximum = first_result

    # روی ادامه iterator حرکت می‌کنیم.
    for result in results_iterator:
        # تعداد نتایج را یک واحد افزایش می‌دهیم.
        count += 1

        # نتیجه جاری را به مجموع اضافه می‌کنیم.
        total += result

        # کمترین مقدار را به‌روزرسانی می‌کنیم.
        minimum = min(minimum, result)

        # بیشترین مقدار را به‌روزرسانی می‌کنیم.
        maximum = max(maximum, result)

    # میانگین را از تقسیم مجموع بر تعداد به دست می‌آوریم.
    average = total / count

    # همه شاخص‌ها را داخل یک دیکشنری برمی‌گردانیم.
    return {
        "count": count,
        "total": total,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
    }


# گزارش آماری تاریخچه را نمایش می‌دهیم.
def show_history_report(history, used_operations):
    """گزارش آماری و فهرست عملیات‌های استفاده‌شده را نمایش می‌دهد."""

    # آمار را محاسبه می‌کنیم.
    statistics = calculate_history_statistics(history)

    # اگر آماری وجود نداشت، تاریخچه خالی است.
    if statistics is None:
        # پیام مناسب نمایش می‌دهیم.
        print("baraye tahiye gozaresh, ebteda chand mohasebe anjam dahid.")

        # اجرای تابع را متوقف می‌کنیم.
        return

    # عنوان گزارش را نمایش می‌دهیم.
    print("\n" + "-" * 60)
    print("gozaresh amari tarikhche")
    print("-" * 60)

    # شاخص‌های آماری را نمایش می‌دهیم.
    print(f"tedad mohasebat: {statistics['count']}")
    print(f"majmu natayej: {format_number(statistics['total'])}")
    print(f"miangin natayej: {format_number(statistics['average'])}")
    print(f"kamtarin natije: {format_number(statistics['minimum'])}")
    print(f"bishtarin natije: {format_number(statistics['maximum'])}")

    # عملیات‌های استفاده‌شده را نیز نمایش می‌دهیم.
    show_used_operations(used_operations)


# تاریخچه را با یک معیار انتخابی مرتب می‌کنیم.
def show_sorted_history(history):
    """تاریخچه را براساس زمان، نتیجه یا نام عملیات مرتب و نمایش می‌دهد."""

    # اگر تاریخچه خالی بود، امکان مرتب‌سازی وجود ندارد.
    if not history:
        # پیام مناسب نمایش می‌دهیم.
        print("tarikhche mohasebat khali ast.")

        # اجرای تابع را پایان می‌دهیم.
        return

    # گزینه‌های مرتب‌سازی را نمایش می‌دهیم.
    print("1. jadidtarin mohasebat")
    print("2. ghadimitarin mohasebat")
    print("3. natije az kuchak be bozorg")
    print("4. nam amaliat")

    # یک انتخاب معتبر دریافت می‌کنیم.
    sort_choice = get_menu_choice(("1", "2", "3", "4"))

    # براساس انتخاب کاربر، یک لیست مرتب‌شده جدید می‌سازیم.
    match sort_choice:
        case "1":
            # با lambda مقدار زمان هر رکورد را به‌عنوان کلید مرتب‌سازی تعیین می‌کنیم.
            sorted_history = sorted(history, key=lambda record: record["created_at"], reverse=True)
        case "2":
            # تاریخچه را از قدیمی به جدید مرتب می‌کنیم.
            sorted_history = sorted(history, key=lambda record: record["created_at"])
        case "3":
            # نتیجه هر رکورد را معیار مرتب‌سازی قرار می‌دهیم.
            sorted_history = sorted(history, key=lambda record: record["result"])
        case _:
            # نام عملیات را معیار مرتب‌سازی قرار می‌دهیم.
            sorted_history = sorted(history, key=lambda record: record["operation"])

    # نسخه مرتب‌شده را با همان تابع نمایش تاریخچه چاپ می‌کنیم.
    show_history(sorted_history)


# تاریخچه را رکوردبه‌رکورد مرور می‌کنیم.
def browse_history_step_by_step(history):
    """با استفاده از iterator و next رکوردهای تاریخچه را یکی‌یکی نمایش می‌دهد."""

    # اگر تاریخچه خالی بود، چیزی برای مرور وجود ندارد.
    if not history:
        # پیام مناسب نمایش می‌دهیم.
        print("tarikhche mohasebat khali ast.")

        # اجرای تابع را متوقف می‌کنیم.
        return

    # از لیست تاریخچه یک iterator می‌سازیم.
    history_iterator = iter(history)

    # تا پایان iterator، رکوردها را یکی‌یکی دریافت می‌کنیم.
    while True:
        # دریافت رکورد بعدی ممکن است StopIteration ایجاد کند.
        try:
            # رکورد بعدی را دریافت می‌کنیم.
            record = next(history_iterator)

            # ورودی‌ها را قالب‌بندی می‌کنیم.
            inputs_text = ", ".join(format_number(value) for value in record["inputs"])

            # اطلاعات رکورد جاری را نمایش می‌دهیم.
            print(
                f"#{record['id']} | {record['operation']} | "
                f"vorudiha: {inputs_text} | natije: {format_number(record['result'])}"
            )

            # برای رفتن به رکورد بعدی از کاربر ورودی می‌گیریم.
            command = input("Enter: record badi | khoruj: payan morur: ").strip().lower()

            # اگر کاربر خروج را وارد کرد، مرور را متوقف می‌کنیم.
            if command == "khoruj":
                # از حلقه مرور خارج می‌شویم.
                break

        # پایان iterator را مدیریت می‌کنیم.
        except StopIteration:
            # پایان تاریخچه را اعلام می‌کنیم.
            print("be payan tarikhche residid.")

            # حلقه را متوقف می‌کنیم.
            break



# مبلغ نامنفی از کاربر دریافت می‌کنیم.
def get_non_negative_number(message):
    """یک عدد صفر یا مثبت را از کاربر دریافت می‌کند."""

    # دریافت ورودی را تا رسیدن به مقدار معتبر ادامه می‌دهیم.
    while True:
        # از تابع عمومی دریافت عدد استفاده می‌کنیم.
        number = get_number(message)

        # اگر عدد صفر یا مثبت بود، آن را می‌پذیریم.
        if number >= 0:
            # مقدار معتبر را برمی‌گردانیم.
            return number

        # مبلغ منفی را رد می‌کنیم.
        print("khata: mablagh ya darsad nemitavanad manfi bashad.")


# یک درصد معتبر بین صفر تا صد دریافت می‌کنیم.
def get_percentage(message):
    """فقط عددی در بازه صفر تا صد را به‌عنوان درصد می‌پذیرد."""

    # دریافت ورودی را تا رسیدن به درصد معتبر ادامه می‌دهیم.
    while True:
        # یک عدد نامنفی دریافت می‌کنیم.
        percentage = get_non_negative_number(message)

        # درصد باید حداکثر صد باشد.
        if percentage <= 100:
            # درصد معتبر را برمی‌گردانیم.
            return percentage

        # مقدار بزرگ‌تر از صد را رد می‌کنیم.
        print("khata: darsad bayad adadi beyn sefr ta sad bashad.")


# تعداد نفرات را به‌صورت عدد صحیح مثبت دریافت می‌کنیم.
def get_positive_integer(message):
    """فقط عدد صحیح بزرگ‌تر از صفر را می‌پذیرد."""

    # دریافت ورودی را تکرار می‌کنیم.
    while True:
        # تبدیل متن به int را امتحان می‌کنیم.
        try:
            # ورودی را به عدد صحیح تبدیل می‌کنیم.
            number = int(input(message))

            # عدد باید بزرگ‌تر از صفر باشد.
            if number <= 0:
                # یک خطای مقدار نامعتبر ایجاد می‌کنیم.
                raise ValueError

            # مقدار معتبر را برمی‌گردانیم.
            return number

        # ورودی نامعتبر را مدیریت می‌کنیم.
        except ValueError:
            # پیام راهنما نمایش می‌دهیم.
            print("khata: lotfan yek adad sahih bozorgtar az sefr vared konid.")


# هزینه‌های جانبی اختیاری را از کاربر دریافت می‌کنیم.
def collect_extra_costs():
    """هر تعداد هزینه جانبی را دریافت می‌کند و داخل یک لیست برمی‌گرداند."""

    # یک لیست خالی برای هزینه‌های جانبی می‌سازیم.
    extra_costs = []

    # توضیح روش ورود هزینه‌ها را نمایش می‌دهیم.
    print("hazinehaye janebi manand ersal ya servis ra vared konid. baraye payan, Enter bezanid.")

    # تا زمانی که کاربر Enter خالی نزند، دریافت هزینه ادامه دارد.
    while True:
        # ورودی را به‌صورت متن دریافت می‌کنیم تا ورودی خالی را تشخیص دهیم.
        raw_value = input("hazine janebi: ").strip()

        # اگر ورودی خالی بود، جمع‌آوری هزینه‌ها پایان می‌یابد.
        if raw_value == "":
            # از حلقه خارج می‌شویم.
            break

        # تبدیل ورودی به عدد ممکن است خطا ایجاد کند.
        try:
            # متن را به عدد اعشاری تبدیل می‌کنیم.
            extra_cost = float(raw_value)

            # مبلغ منفی قابل قبول نیست.
            if extra_cost < 0:
                # یک خطای مقدار نامعتبر ایجاد می‌کنیم.
                raise ValueError

            # هزینه معتبر را به لیست اضافه می‌کنیم.
            extra_costs.append(extra_cost)

        # ورودی نامعتبر را مدیریت می‌کنیم.
        except ValueError:
            # پیام خطا نمایش می‌دهیم.
            print("khata: hazine janebi bayad yek adad sefr ya mosbat bashad.")

    # لیست هزینه‌های ثبت‌شده را برمی‌گردانیم.
    return extra_costs


# مبلغ نهایی صورت‌حساب را محاسبه می‌کنیم.
def calculate_final_bill(base_amount, *extra_costs, **rates):
    """مبلغ پایه، هزینه‌های متغیر و درصدهای اختیاری را دریافت و جزئیات صورتحساب را برمی‌گرداند."""

    # از معتبر بودن مبلغ پایه اطمینان پیدا می‌کنیم.
    if base_amount < 0:
        # مبلغ منفی را رد می‌کنیم.
        raise ValueError("mablagh paye nemitavanad manfi bashad.")

    # بررسی می‌کنیم هیچ هزینه جانبی منفی نباشد.
    if any(extra_cost < 0 for extra_cost in extra_costs):
        # هزینه جانبی منفی را رد می‌کنیم.
        raise ValueError("hazinehaye janebi nmy tvannd manfi bashnd.")

    # همه نرخ‌های درصدی باید در بازه صفر تا صد باشند.
    if any(rate < 0 or rate > 100 for rate in rates.values()):
        # نرخ نامعتبر را رد می‌کنیم.
        raise ValueError("drsdha bayad beyn sefr ta sad bashnd.")

    # تمام هزینه‌های جانبی دریافت‌شده با *args را جمع می‌کنیم.
    extra_costs_total = sum(extra_costs)

    # مبلغ اولیه شامل مبلغ پایه و هزینه‌های جانبی است.
    subtotal = base_amount + extra_costs_total

    # درصد تخفیف را از دیکشنری **kwargs می‌خوانیم؛ مقدار پیش‌فرض صفر است.
    discount_percent = rates.get("discount_percent", 0)

    # درصد مالیات را از دیکشنری نرخ‌ها می‌خوانیم.
    tax_percent = rates.get("tax_percent", 0)

    # درصد انعام را از دیکشنری نرخ‌ها می‌خوانیم.
    tip_percent = rates.get("tip_percent", 0)

    # مبلغ تخفیف را براساس مبلغ اولیه محاسبه می‌کنیم.
    discount_amount = subtotal * discount_percent / 100

    # مبلغ پس از تخفیف را محاسبه می‌کنیم.
    discounted_subtotal = subtotal - discount_amount

    # مالیات را روی مبلغ پس از تخفیف محاسبه می‌کنیم.
    tax_amount = discounted_subtotal * tax_percent / 100

    # انعام را روی مبلغ پس از تخفیف محاسبه می‌کنیم.
    tip_amount = discounted_subtotal * tip_percent / 100

    # مبلغ نهایی را با افزودن مالیات و انعام به دست می‌آوریم.
    final_total = discounted_subtotal + tax_amount + tip_amount

    # تمام جزئیات محاسبه را داخل یک دیکشنری برمی‌گردانیم.
    return {
        "base_amount": base_amount,
        "extra_costs_total": extra_costs_total,
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "tax_amount": tax_amount,
        "tip_amount": tip_amount,
        "final_total": final_total,
    }


# فرایند کامل تقسیم صورت‌حساب را اجرا می‌کنیم.
def run_bill_splitter(history, used_operations):
    """اطلاعات صورت‌حساب را دریافت، مبلغ نهایی را محاسبه و بین افراد تقسیم می‌کند."""

    # عنوان بخش را نمایش می‌دهیم.
    print("\n" + "-" * 60)
    print("taghsim hushmand surathesab")
    print("-" * 60)

    # مبلغ پایه صورت‌حساب را دریافت می‌کنیم.
    base_amount = get_non_negative_number("mablagh paye surathesab: ")

    # هر تعداد هزینه جانبی را داخل یک لیست دریافت می‌کنیم.
    extra_costs = collect_extra_costs()

    # درصد تخفیف را دریافت می‌کنیم.
    discount_percent = get_percentage("darsad takhfif: ")

    # درصد مالیات را دریافت می‌کنیم.
    tax_percent = get_percentage("darsad malyat: ")

    # درصد انعام را دریافت می‌کنیم.
    tip_percent = get_percentage("darsad anaam: ")

    # تعداد افراد را دریافت می‌کنیم.
    people_count = get_positive_integer("tedad afrad: ")

    # نرخ‌های اختیاری را داخل یک دیکشنری قرار می‌دهیم.
    rates = {
        "discount_percent": discount_percent,
        "tax_percent": tax_percent,
        "tip_percent": tip_percent,
    }

    # لیست هزینه‌ها را با * و دیکشنری نرخ‌ها را با ** باز می‌کنیم.
    bill_details = calculate_final_bill(base_amount, *extra_costs, **rates)

    # سهم هر نفر را از تقسیم مبلغ نهایی بر تعداد افراد محاسبه می‌کنیم.
    per_person_amount = bill_details["final_total"] / people_count

    # جزئیات محاسبه را نمایش می‌دهیم.
    print("\njoziyat surathesab")
    print(f"mablagh paye: {format_number(bill_details['base_amount'])}")
    print(f"jam hazinehaye janebi: {format_number(bill_details['extra_costs_total'])}")
    print(f"jam avvaliye: {format_number(bill_details['subtotal'])}")
    print(f"mablagh takhfif: {format_number(bill_details['discount_amount'])}")
    print(f"mablagh maliat: {format_number(bill_details['tax_amount'])}")
    print(f"mablagh anam: {format_number(bill_details['tip_amount'])}")
    print(f"mablagh nahai: {format_number(bill_details['final_total'])}")
    print(f"sahm har nafar: {format_number(per_person_amount)}")

    # ورودی‌های کلیدی را برای تاریخچه داخل یک تاپل قرار می‌دهیم.
    history_inputs = (base_amount, people_count, discount_percent, tax_percent, tip_percent)

    # نتیجه تقسیم صورت‌حساب را در تاریخچه ذخیره می‌کنیم.
    save_to_history(
        history,
        used_operations,
        "taghsim surathesab",
        history_inputs,
        per_person_amount,
    )


# منوی برنامه را نمایش می‌دهیم.
def show_menu():
    """عملیات محاسباتی و مدیریت تاریخچه را نمایش می‌دهد."""

    # منوی کامل را چاپ می‌کنیم.
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


# عملیات‌های دوورودی را اجرا می‌کنیم.
def calculate_binary_operation(choice, first_number, second_number):
    """یکی از عملیات‌های دوورودی را اجرا می‌کند."""

    # براساس انتخاب کاربر، تابع مناسب را فراخوانی می‌کنیم.
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
    """یکی از عملیات‌های تک‌ورودی را اجرا می‌کند."""

    # براساس انتخاب کاربر، عملیات را انجام می‌دهیم.
    match choice:
        case "8":
            return square_root(number)
        case "9":
            return absolute_value(number)
        case _:
            return None


# تابع اصلی برنامه را تعریف می‌کنیم.
def main():
    """محاسبات و مدیریت تاریخچه را تا زمان خروج کاربر اجرا می‌کند."""

    # تاریخچه را در یک لیست نگهداری می‌کنیم؛ ترتیب محاسبات در لیست حفظ می‌شود.
    history = []

    # نام عملیات‌های استفاده‌شده را در یک مجموعه نگهداری می‌کنیم تا تکراری نباشند.
    used_operations = set()

    # گزینه‌های معتبر منو را در یک تاپل قرار می‌دهیم.
    valid_choices = tuple(str(number) for number in range(0, 18))

    # عملیات‌های نیازمند دو عدد را در یک مجموعه قرار می‌دهیم.
    binary_choices = {"1", "2", "3", "4", "5", "6", "7"}

    # عملیات‌های نیازمند یک عدد اعشاری را در یک مجموعه قرار می‌دهیم.
    unary_choices = {"8", "9"}

    # اجرای برنامه را تا انتخاب خروج ادامه می‌دهیم.
    while True:
        # منو را نمایش می‌دهیم.
        show_menu()

        # انتخاب معتبر دریافت می‌کنیم.
        choice = get_menu_choice(valid_choices)

        # گزینه خروج را مدیریت می‌کنیم.
        if choice == "0":
            # پیام خداحافظی نمایش می‌دهیم.
            print("az hamrahi shoma moteshakkerim. khodahafez!")

            # حلقه را متوقف می‌کنیم.
            break

        # گزینه نمایش تاریخچه را مدیریت می‌کنیم.
        if choice == "11":
            # تاریخچه را نمایش می‌دهیم.
            show_history(history)

            # به ابتدای حلقه برمی‌گردیم.
            continue

        # گزینه پاک کردن تاریخچه را مدیریت می‌کنیم.
        if choice == "12":
            # تاریخچه و مجموعه عملیات‌ها را پاک می‌کنیم.
            clear_history(history, used_operations)

            # به ابتدای حلقه برمی‌گردیم.
            continue

        # گزینه نمایش عملیات‌های استفاده‌شده را مدیریت می‌کنیم.
        if choice == "13":
            # عملیات‌ها را نمایش می‌دهیم.
            show_used_operations(used_operations)

            # به ابتدای حلقه برمی‌گردیم.
            continue

        # گزینه گزارش آماری را مدیریت می‌کنیم.
        if choice == "14":
            # گزارش آماری را نمایش می‌دهیم.
            show_history_report(history, used_operations)

            # به ابتدای حلقه برمی‌گردیم.
            continue

        # گزینه نمایش مرتب‌شده را مدیریت می‌کنیم.
        if choice == "15":
            # تاریخچه مرتب‌شده را نمایش می‌دهیم.
            show_sorted_history(history)

            # به ابتدای حلقه برمی‌گردیم.
            continue

        # گزینه مرور مرحله‌ای را مدیریت می‌کنیم.
        if choice == "16":
            # تاریخچه را با iterator مرور می‌کنیم.
            browse_history_step_by_step(history)

            # به ابتدای حلقه برمی‌گردیم.
            continue

        # گزینه تقسیم صورت‌حساب را مدیریت می‌کنیم.
        if choice == "17":
            # فرایند تقسیم صورت‌حساب را اجرا می‌کنیم.
            run_bill_splitter(history, used_operations)

            # به ابتدای حلقه برمی‌گردیم.
            continue

        # عملیات محاسباتی ممکن است خطا ایجاد کند؛ بنابراین از try استفاده می‌کنیم.
        try:
            # عنوان فارسی عملیات انتخاب‌شده را دریافت می‌کنیم.
            operation_title = get_operation_title(choice)

            # عملیات‌های دوورودی را اجرا می‌کنیم.
            if choice in binary_choices:
                # عدد اول را دریافت می‌کنیم.
                first_number = get_number("adad aval ra vared konid: ")

                # عدد دوم را دریافت می‌کنیم.
                second_number = get_number("adad dovom ra vared konid: ")

                # ورودی‌ها را داخل یک تاپل قرار می‌دهیم.
                input_values = (first_number, second_number)

                # نتیجه را محاسبه می‌کنیم.
                result = calculate_binary_operation(choice, first_number, second_number)

            # عملیات‌های تک‌ورودی را اجرا می‌کنیم.
            elif choice in unary_choices:
                # عدد را دریافت می‌کنیم.
                number = get_number("adad ra vared konid: ")

                # ورودی را داخل یک تاپل تک‌عضوی قرار می‌دهیم.
                input_values = (number,)

                # نتیجه را محاسبه می‌کنیم.
                result = calculate_unary_operation(choice, number)

            # گزینه باقی‌مانده فاکتوریل است.
            else:
                # عدد صحیح نامنفی دریافت می‌کنیم.
                number = get_non_negative_integer("adad sahih sefr ya mosbat ra vared konid: ")

                # ورودی را داخل یک تاپل تک‌عضوی قرار می‌دهیم.
                input_values = (number,)

                # فاکتوریل را محاسبه می‌کنیم.
                result = factorial_recursive(number)

            # نتیجه را قالب‌بندی و نمایش می‌دهیم.
            print(f"natije: {format_number(result)}")

            # محاسبه موفق را در تاریخچه ذخیره می‌کنیم.
            save_to_history(history, used_operations, operation_title, input_values, result)

        # خطاهای تقسیم بر صفر را مدیریت می‌کنیم.
        except ZeroDivisionError as error:
            # پیام خطا را نمایش می‌دهیم.
            print(f"khata: {error}")

        # خطاهای مقدار نامعتبر را مدیریت می‌کنیم.
        except ValueError as error:
            # پیام خطا را نمایش می‌دهیم.
            print(f"khata: {error}")


# بررسی می‌کنیم فایل به‌صورت مستقیم اجرا شده باشد.
if __name__ == "__main__":
    # تابع اصلی را اجرا می‌کنیم.
    main()
