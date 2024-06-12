from . import jalali
from django.utils import timezone


def jalali_converter(time):
    jalali_months ={
        '1': 'فروردین',
        '2': 'اردیبهشت',
        '3': 'خرداد',
        '4': 'تیر',
        '5': 'مرداد',
        '6': 'شهریور',
        '7': 'مهر',
        '8': 'آبان',
        '9': 'آذر',
        '10': 'دی',
        '11': 'بهمن',
        '12': 'اسفند',
    }
    time = timezone.localtime(time)
    time_to_str = '{},{},{}'.format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    output = '{} {} {}, ساعت {}:{}'.format(
        time_to_tuple[2],
        jalali_months[str(time_to_tuple[1])],
        time_to_tuple[0],
        time.hour,
        time.minute
    )
    return output