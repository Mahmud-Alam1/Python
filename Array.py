'''
my_list=[]
n=int(input("enter the n size value"))
for i in range(n):
    element=int(input("enter the element:-"))
   # element=int(input(f"enter the element:{i+1}"))
    my_list.append(element)
print(my_list)
# for i in my_list:
#    print(i,end=" ")

# i=0
# while(i<len(my_list)):
#     print(my_list[i],end=" ")
#     i+=1
'''
    

items=[4,3,8,3,2,3]
print("list of item :",items)
x=int(input("enter the number u want to seach"))   #3
i=pos=0

while i<len(items):                 #0<=5      1<=5     2<=5      3<=5      4<=5       5<=5
    if items[i]==x:                 #4==3      3==3     8==3      3==3      2==3       3==3
        pos=i
        print("item found at position,",pos) #1 3  5 position of 3 in items

    i=i+1
if(pos==0):
    print("item not found")   



# sum of array element using builting function
arr=[1,2,3]
print(sum(arr))


arr=['e','p','t','e','t']
x='e'
indices=[]
for i in range(len(arr)):
    if arr[i]==x:
        indices.append(i)
if indices:
    print("element 'e' found at indeics",indices)
else:
    print("element 'e' not found at indeics",indices)
