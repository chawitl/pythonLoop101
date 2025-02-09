s = input("enter:")
re = ("")

for i in range(len(s)-1,-1,-1):
    re += s[i]
if re == s:
    print("palindrome")
else:
    print("not palindrome")
