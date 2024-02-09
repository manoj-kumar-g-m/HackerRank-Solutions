# if year % by 400 and 100 its leap year
# if number is visible by 4 and not visible by 100 it's also a leap yer

year = int(input("Enter the year:"))
if year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
