N = int(input("Enter a number: "))
count=0
num=N
if num==0:
    count=1
else:
    while num>0:
        count+=1
        num//=10
print("count of digits: ", count)
