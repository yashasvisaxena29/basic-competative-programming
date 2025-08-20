n=int(input("enter a number: " ))
rev=0
while(n>0):
     sum=n%10
     n=n//10
     rev=rev*10+sum
print(rev)
