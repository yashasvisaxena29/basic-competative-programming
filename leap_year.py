year=int(input("enter year: "))
if year%4==0 and year%100!=0:
    print("it's a leap year")
else:
    print("it's not a leap year")
