
""" def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Science']
info = {'name': 'John Doe', 'age': 20}

student_info(*courses, **info) """

# Number of days por month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return the number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days(month)

print(is_leap(2020))
