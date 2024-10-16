N=int(input("Enter the no. of elements"))
k=int(input("enter the k"))
a=[]
for i in range(0,N):
    b=int(input("enter the element"))
    a.append(int(b))
x=0
for i in range(0,N):
    x=x+a[i]
print("the number to subtract or add is: ",x%k)