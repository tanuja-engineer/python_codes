def palindrome(s,left,right):
    if left>=right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome(s,left+1,right-1)
s=input("enter a string:").lower()
if palindrome(s,0,len(s)-1):
    print("palindrome")
else:
    print("not palindrome")
