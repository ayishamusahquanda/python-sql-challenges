def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 ==0:
        return True
    return False


# ---Tests---
for y in [1900, 2000, 2024, 2100]:
    print(y, is_leap_year(y))