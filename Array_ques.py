'''#find the largest and smallest number using array?
l=[]
n=int(input("Enter size of list:-"))
for x in range(n):
    x=int(input("Enter element of list:"))
    l.append(x)
largest=l[0]
smallest=l[0]
for i in range(n):
    if l[i]>largest:
        largest=l[i]
    if l[i]<smallest:
        smallest=l[i]
print("largest element:-", largest)
print("largest element:-", smallest)
'''


'''
#find the index min number and max ?
arr=[12,89,4,0,4,80,8]
print(arr.index(min(arr)))
#print(min(arr))

print(arr.index(max(arr)))
#print(max(arr))
'''


# find the second largest number?
numbers=[12,23,45,65,34]
largest=0
second_largest=0

for num in numbers:
    if num>largest:             
        second_largest=largest
        largest=num
    elif num > second_largest:
        second_largest=num

print(second_largest)


'''
#find the smallest number??
numbers=[2,1,13,24,11]
largest=10
second_largest=10

for num in numbers:
    if num<largest:
        second_largest=largest
        largest=num
    elif num <second_largest:
        second_largest=num

print(second_largest)
'''

'''
#find the linear search?
numbers=[1, 4, 4, 4, 5]
target=4                # write the target value(example:-23,45,1,4,5)
result=0
for i in range(0,len(numbers)): #range(o,5)
    if numbers[i]==target:
        result=i
        print(result)

if result==0:
    print(f"{target} is not present")
'''

'''
#write the prog.to even or odd
input_number=input(("Enter number sepated by spaces:-"))
number=list(map(int,input_number.split()))
even_number=[]
odd_number=[]
for num in number:
    if num%2==0:
        even_number+=[num]

    else:
        odd_number+=[num]
print("even_number:",end=" ")
print(*even_number,end=" ") #remove the square breaket[]
print("\n odd_number:",end=" ")
print(*odd_number,end=" ")
'''

'''
input_number=input(("Enter number sepated by spaces:-"))
number=list(map(int,input_number.split()))
evensum=0
oddsum=0
for num in number:
    if num%2==0:
        evensum+=[num]

    else:
        oddsum+=[num]
print("even_number:",end=" ")
print(evensum,end=" ") #remove the square breaket[]
print("\n odd_number:",end=" ")
print(oddsum,end=" ")
'''
'''
input_numbers=input(("Enter number sepated by spaces:-"))
numbers=list(map(int,input_numbers.split()))

total=0
count=0
for num in numbers:
    total+=num
    count+=1
    avg=total//count

print(total,avg)
'''


