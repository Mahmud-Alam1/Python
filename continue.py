'''
for i in range(1,11):
    if i==5:
        continue
    print(i)
'''
'''
i=1
while i<=5:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1
'''

'''
sum=0
for val in range(1,9):
    if val==4:
        continue
    sum+=val
print(sum)
'''
'''
number=5
for i in range(1,11):
    result=number*i
    if result%3==0:
        continue
    print(number,"*",i,"=",number*i)
'''
'''
for i in range(1,4):
    for j in range(4):
        if i==2 and j==2:
            continue
        print(i,j)
'''
'''
for i in range(1,4):
    for j in range(4):
        if i==2 or j==2:
            continue
        print(i,j)
'''
'''
n=int(input("Enter the any value:-"))
for i in range(0,n,2):
    if i==2:
        continue
    print(i,end=' ')
'''   
#this is odd number
i=1                  #i=0  then event number
while i<=10:
    if i==2:         #if i==1 
        i+=1
        continue
    print(i)
    i+=2
