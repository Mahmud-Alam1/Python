#INTERVIEW QUES:- 
'''
# Q. without using modules(%) and division(/) operator function 
def is_leap(year): 
    i=4
    while i<=year:
        if i==year:
            return True
        i+=4

    return False

year=2024 #8
if is_leap(year): #8 true
    print(year,"is a leap year.")

else:
    print(f"{year} is not a leap year.")
'''



#Q. write the program to calculate the power without using POW function
'''   
base=int(input("Enter the base no.:-")) #2
power=int(input("Enter the power:-")) #3

result=1
for i in range(power): #0<3
    result*=base  #1*2=2*2=4*2=8
 
print("result:",result) #8
'''
'''
#Q.
even_sum=0
odd_sum=0

while True:
    number=int(input("Enter the number:-")) #2 # 3 #6  #5

    if number%2==0:  #2%2==0     6%2==0
        even_sum+=number  #0+2=2   2+6=8
    else:
        odd_sum+=number  #0+3=3   #3+5=8
    choice=input("Do you want to continue?(y/n):").lower() # Get user choice y y n

    if choice!="y":
        break

print("Sum of even number:",even_sum)
print("Sum of odd number:",odd_sum)
'''

# find the largest and smallest number of array?
arr=[]
n=int(input("Enter size of array:-"))
for x in range(n):
    
    x=int(input("Enter element of array:"))
    arr.append(x)
largest=arr[0]
smallest=arr[0]
for i in range(n):
    if arr[i]>largest:
        largest=arr[i]
    if arr[i]<smallest:
        smallest=arr[i]
    
print("largest element in array is largest", largest)
print("largest element in array is smallest", smallest)