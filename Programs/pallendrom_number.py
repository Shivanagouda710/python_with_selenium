num=121
tem = num
rem =0
digit=0

while(num!=0):
    digit=num%10
    rem=(rem*10)+digit
    num=int(num/10)

  

if(tem==rem):
    print("Yes Pallendrome ..!!!")
else:
    print("Not Pallendrome ..!!!")

