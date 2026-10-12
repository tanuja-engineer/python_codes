n=int(input("Enter the number:"))
arr=[]
sum=0
for i in range(n-1):
    num=int(input("Enter the number:"))
    arr.append(num)
    sum=sum+num
total=n*(n+1)//2
missing=total-sum
print("Missing number=",missing)