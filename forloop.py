
'''n=int(input("Enter the N values:-"))
for i in range (0,n+1,2):
    print(i, end=" ")
'''

'''
# Write a prog to create table 
    
n=int (input("Enter the N values:-"))
for i in range (1,11):
    print(n,"*",i,"=",n*i)
    '''



'''
 # Square function
n=int (input("Enter the N values:-"))
for i in range (1,n+1):
    print(i,"*",i,"=",i*i)
'''

'''
# write a program to display sum of n number without range
sum=0
number = [2,3,2]

for val in number:
    sum = sum + val
    print("sum=", sum)

'''

'''
# write program to print square of n number:-
n=int(input("enter the n nmber:-"))
sum=2
for i in range (1, n+1):
    sum = sum+i
print(sum)
'''
'''
n=int(input("enter the n nmber:-"))
fact=1
for i in range (1, n+1):
    fact = fact*i
print(fact)
'''

'''
n=int(input("enter the n nmber:-"))
fact=1
for i in range (n,1,-1):
    fact = fact*i
print(fact)
'''

'''
# factorial function
import math
n=int(input("enter the N number"))

print(math.factorial(n))
'''

'''
# fibrication
n=int(input("Enter the N value:-")) #8
first=0
second=1
for i in range(n):        #1<8    #2<8   #3<8

    print(first, end=" ") #0      #0
    temp=first            #0      #1
    first=second          #1      #1
    second=temp+first     #0+1=1  #1+1=2
'''

'''
#x=int(input("Enter the of x value:-"))
name="alam"
for i in range (1,11):
     print(name)
'''   

'''
# to display the calender
     
import calendar
year=int(input("Enter the Year"))
for i in range(1, 13):
     print(calendar.month(year,i))
'''            
'''
#reversed calendar
import calendar
year=int(input("Enter the Year:-"))
for i in range(12,0-1):
    print(calendar.month(year,i))

'''
'''
#pattern
row = 5
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")
    '''

'''
#pattern
row = 5
for i in range(row+1,0,-1):     #* * * * * *
    for j in range(1, i+1):     #* * * * *
        print("*",end=" ")      #* * * *
    print(" ")                  #* * *
                                #* *
                                #*
'''

'''
n=int(input("Enter the of row:-"))  #1
for i in range(n):                  #1 2
    for j in range(i+1):            #1 2 3
        print(j+1,end=" ")          #1 2 3 4 
    print(" ")                      #1 2 3 4 5 
'''

'''
n=int(input("Enter the of row:-"))  #1
for i in range(n):                  #2 1 
    for j in range(i,-1,-1):        #3 2 1
        print(j+1,end=" ")          #4 3 2 1 
    print(" ")                      #5 4 3 2 1


n=int(input("Enter the of row:-"))  #1
for i in range(n):                  #2 2
    for j in range(i,-1,-1):        #3 3 3
        print(i+1,end=" ")          #4 4 4 4
    print(" ")                      #5 5 5 5 5 
'''


num=int(input('Enter the number:'))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
        print(i)

if count==2:
    print("prime")
else:
    print("not prime")
'''
'''
list1=[1,2,3,4]
evencount=0
oddcount=0
for num in list1:
    if num%2==0:
        evencount+=1

    else:
        oddcount+=1
print("even numbers in list:",evencount)
print("odd numbers in list:",oddcount)    
'''

minimum=int(input("Enter the minimum value:-"))
maximum=int(input("Enter the maximum value:-"))
for num in range(minimum, maximum):
    temp=num
    reverse=0

    while(temp>0):
        reminder=temp%10

        reverse=(reverse*10)+reminder

        temp=temp//10

    if(num==reverse):
        print(num, end=" ")
'''
