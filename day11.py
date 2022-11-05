second = 1
minute = second * 60
hour = minute * 60
day = hour * 24
week = day * 7
month = week * 4
year = day * 365
leapYear = day * 366
print("Let's see how many seconds are in a year!")
answer = input("Is it a normal year or a leap year?")
if answer == "normal":
    print("There are", year, "seconds in a year!")
else:
    print("There are", leapYear, "seconds in a leap year!")
