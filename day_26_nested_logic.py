from datetime import datetime

def calculate(due_date, return_date): 
    # if returns before the due date
    if due_date >= return_date:
        return 0
    # for late, calculate the time differences
    year_lapse = return_date.year - due_date.year
    month_lapse = return_date.month - due_date.month
    day_lapse = return_date.day - due_date.day
    if year_lapse > 0:
        return 10000
    elif month_lapse > 0:
        return month_lapse * 500
    else:
        return day_lapse * 15

# get inputs
r = input().split(" ")
d = input().split(" ")
return_date = datetime(int(r[2]), int(r[1]), int(r[0]))
due_date = datetime(int(d[2]), int(d[1]), int(d[0]))
print(calculate(due_date, return_date))