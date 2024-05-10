





name ="madaum knows malayalam very well"
reversedline= name[len(name)-1::-1]

word=name.split(" ")
reverseword=reversedline.split(" ")

# print(word[2])
# print(reverseword[2])


for x in word:
    for y in reverseword:
        if(x==y):
            print(x,y)



