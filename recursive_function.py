'''
#WAP to find the factorial using recursive function: with argument and return values.
def factorial(n):  #5
    if n==0 or n==1:  #5==0 or 5==1 (f)
        return n
    else:
        return n*factorial(n-1)
        #5*factorial(4)
        #4*factorial(3)
        #3*factorial(2)
        #2*factorial(1)
        #2*3*4*5=120
    
n=int(input("enter N value:-"))
print(factorial(n))
#2*3*4*5=120
'''

'''
def add(value):
    value = 20
    print("inside method call=",value)#10

def main():
    num=10
    print("before method call=",num) 
    add(num)
    print("after method call=",num)
main()
'''

def fibonacci(n):
    if n==1:
        return 0     
    elif n==2:
        return 1
    
    else:
        return fibonacci(n-1)+fibonacci(n-2)
                    #2            #1   1+0=1
n=int(input("Enter the number of terms:-"))
for i in range(1,n+1):
    print(fibonacci(i),end=" ")   #0  1  1



'''
num=120
i=1 #5
while i!=num: #5!=5
    num=num//i #120//1   120//2=60  60//3  20//4=5
    i+=1

print("120 is a factorial of =",num)
'''

'''
def print_sorted_reverse(arr):
    arr.sort()
    arr.sort(reverse=False)
    print(arr)
    print(arr[::-1])
    arr.sort(reverse=True)
    print(arr)
    #for num in reversed(arr):
    #   print(num,end=" ")

arr=[5, 2, 8, 1, 9]
print_sorted_reverse(arr)
'''
'''
def sum_of_digit(num):
    sum=0
    sum+=num%10
    num//=10
    sum+=num%10
    num//=10
    sum+=num%10
    return sum

num=123
result=sum_of_digit(num)
print("sum of digits of",num,"is",result)
'''