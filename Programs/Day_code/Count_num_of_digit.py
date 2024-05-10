

num=47509

count=0
while(num!=0):
    count=count+1
    digit=num%10
    num=int(num/10)
    print(digit,"---",count)


