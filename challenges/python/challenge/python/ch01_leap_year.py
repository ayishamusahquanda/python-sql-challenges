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
    print(is_leap_year(0))              # --- Test for year 0 (mathematically correct and returns True)---
    print(is_leap_year(-2024))          # --- Test for negative year (modulos works on negatives so it returns True)---
    print(is_leap_year("2024"))         # --- Test for string input (throws TypeError because string cannot be used with modulo operator)---