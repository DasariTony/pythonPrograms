#leap year 
year=int(input("Enter year:"))
if (year%4==0 and year%400) or year%100!=100:
    print("leap Year")
else:
    print("Not leap Year")