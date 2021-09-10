def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        if year % 400 == 0:
            return True
        else:
            return False
    return False

year = int(input())
print (is_leap(year))