#print(list(range(0,6)))
for i in range(1,10,2):
    print(i)
for i in range(1,10,2):
    print(i*i,end="")
#
for i in range(1,n+1):
    print(i)
#odd
for i in range(1,n+1,2):
    print(i)

A = int(input("Enter A: "))
B = int(input("Enter B: "))

ans = 1
for i in range(B):
    ans = ans * A

print(ans)