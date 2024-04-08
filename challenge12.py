def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year")
      else:
        print("Not leap year")
    else:
      print("Leap year")
  else:
    print("Not leap year")
  
# TODO: Add more code here 👇
def days_in_month(year_num ,month_num):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  total_days = 0
  if month_num <= 12:
    for i in range (0,month_num - 1):
      total_days += month_days[i]
  print(total_days)

#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

