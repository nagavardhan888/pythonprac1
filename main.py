# Calculating Plant Growth Stages
n = int(input("enter the number of days: "))
n1=0;
n2 =1;
print(n1,n2,end=" ")
for i in range(2,n+1):
    n = n1+n2
    n1=n2
    n2=n
    print(n,end=" ")