str1=input("enter first string:")
str2=input("enter second string:")
str1 = str1.lower().replace("","")
str2 = str2.lower().replace("","")
if len(str1)!=len(str2):
    print("not anagrams")
else:
    count={}
    for ch in str1:
        if ch in count:
            count[ch]=count[ch]+1
        else:
            count[ch]=2
    for ch in str1:
        if ch in count:
            count[ch]=count[ch]-1
        else:
            count[ch]=-1
    result=True
    for ch in count:
        if count[ch]!=0:
            result=False
    if result:
        print("Anagrams")
    else:
        print("not anagrams")