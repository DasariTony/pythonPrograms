n1=int(input("Enter n1 number:"))
n2=int(input("Enter n2 number:"))
n3=int(input("Enter n3 number:"))
def add():
    return n1+n2+n3
def sub():
    return n1-n2
def mul():
    return n1*n2
def div():
    if n2==0:
        print("Error=You have Entered n2 as 0")
    return n1/n2
def avg():
    return (n1+n2+n3)/3
result_add=add()
result_sub=sub()
result_mul=mul()
result_div=div()
result_avg=avg()
print("additoin :",result_add)
print("substraction :",result_sub)
print("Multiplication :",result_mul)
print("Division :",result_div)
print("Avarage :",result_avg)

