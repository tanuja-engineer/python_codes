def calculate(numbers):
    total=0
    count=0
    largest=0

    for num in numbers:
        if num>=0 and num%2==0:
            square=num*num
            total=total+square
            count=count+1

            if square>largest:
                largest=square
    if count==0:
        return 0,0,None
    return total,count,largest
numbers=[-2,1,2,3,4,6,-8]
total,count,largest=calculate(numbers)
print("Total=",total)
print("Count=",count)
print("Largest=",largest)