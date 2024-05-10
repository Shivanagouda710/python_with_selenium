

par="{([])}{}"
l=[]
for x in par:
    l.append(x)





# l=["{","[","]","(",")","}"]
# l=["{","]"]
stack=[]

def change(operator):
    if(operator=="{"):
    #   print("}")
      stack.append("}")
    elif(operator=="["):
        # print("]")
        stack.append("]")
    elif(operator=="("):
        # print(")")
        stack.append(")")
    else:
        return False



for x in l:
    if(change(x)==False):
        print(x,"-" ,"changeit")
        if(x==stack[-1]):
            stack.pop()

    else:
        print(x,"-" ,"correct")

print(stack)

if(len(stack)==0):
    print("Valid paranthis")
else:
    print("Not a valida parenthis")