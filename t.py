
# function which return reverse of a string
name = input("")
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
ans = isPalindrome(name)
 
if ans:
    print("Yes")
else:
    print("No")
    
