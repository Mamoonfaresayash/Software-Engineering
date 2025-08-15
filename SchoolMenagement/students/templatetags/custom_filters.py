# student_filters.py

from django import template

register = template.Library()

@register.filter(name='status_icon')
def status_icon(value):
    """تحويل نعم / لا إلى رموز ✅ / ❌"""
    if value == "نعم":
        return "✅"
    elif value == "لا":
        return "❌"
    return value

@register.filter(name='age_group')
def age_group(age):
    """
    تصنيف الطلاب حسب العمر:
    - أقل من 20 → ناشئ
    - 20 إلى 22 → شاب
    - أكبر من 22 → بالغ
    """
    try:
        age = int(age)
        if age < 20:
            return "🟢 ناشئ"
        elif 20 <= age <= 22:
            return "🔵 شاب"
        else:
            return "🔴 بالغ"
    except (ValueError, TypeError):
        return "❓ غير معروف"
