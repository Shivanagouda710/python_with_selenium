str1="silent"
str2="listen"

l1=list(str1)
l1.sort()
l2=list(str2)
l2.sort()


s1 = "".join(l1)
s2 = "".join(l2)

if(s1==s2):
    print("Yes . Anagram ..!!!!!")
else:
    print("Not . Anagram ..!!!!!")
