class palistr:
    def __init__(self):
        self.isPali=False
    def chkpalindrome(self,mystr):
        if mystr == mystr[::-1]:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali
class paliInt(palistr):
    def __init__(self):
        self.isPali=False
    def chkpalindrome(self,val):
        temp=val
        rev=0
        while temp!=0:
            dig=temp%10
            rev=(rev*10)+dig
            temp=temp//10
        if val==rev:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali
st=input("enter the string")
stObj=palistr()
if stObj.chkpalindrome(st):
    print("given string is a palindrome")
else:
    print("given string is not palindrome")
val=int(input("enter a integer"))
intObj=paliInt()
if intObj.chkpalindrome(val):
    print("given integer is a palindrome")
else:
    print("given integer is not a palindrome")