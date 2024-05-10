

# overloading not suport in python but alternative way is below
class cal:
    
    def add(self,a=None ,b=None):
        if(a!=None and b!=None):
            print(a+b)
        elif(a!=None):
            print(a)
        elif(b!=None):
            print(b)
        else:
            print("Nothing")

c =cal()
c.add(2)

