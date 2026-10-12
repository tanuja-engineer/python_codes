largest=0
second=0
numbers=[10,20,5,8,15,12]
for num in numbers:
    if num>largest:
        second=largest
        largest=num
    elif num<largest and num>second:
        second=num
print("second largest number:",second)
