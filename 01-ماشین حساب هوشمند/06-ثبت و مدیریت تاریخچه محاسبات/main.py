# ماژول math ابزارهای محاسباتی آماده مانند جذر را در اختیار ما قرار می‌دهد.
import math

# کلاس datetime برای ثبت زمان انجام هر محاسبه استفاده می‌شود.
from datetime import datetime

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
    print("0. khoruj")
    print("=" * 60)

# تابع اصلی برنامه را تعریف می‌کنیم.
def main():
    """محاسبات و مدیریت تاریخچه را تا زمان خروج کاربر اجرا می‌کند."""

    # تاریخچه را در یک لیست نگهداری می‌کنیم؛ ترتیب محاسبات در لیست حفظ می‌شود.
    history = []

    # نام عملیات‌های استفاده‌شده را در یک مجموعه نگهداری می‌کنیم تا تکراری نباشند.
    used_operations = set()

    # گزینه‌های معتبر منو را در یک تاپل قرار می‌دهیم.
    valid_choices = tuple(str(number) for number in range(0, 14))

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
