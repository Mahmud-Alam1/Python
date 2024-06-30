# Function to find the largest and smallest of three numbers
'''
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
print(largest(5,3,8))

def smallest(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    elif c<a and c<b:
        return c
print(smallest(5,3,8))
'''

'''
def add (m,n):
    return m-(-n)

def multiply(m,n):
    result=0
    for i in range (1,n+1):
        result+=m
    return result

def subtract(m,n):
    result=0
    while m>=n:
        m-=n
        result+=1
    return m,result

def main():
    print("Enter a value:")
    m=int(input())
    n=int(input())

    print("Enter choice: 1.add 2.mul 3.div/quot")
    choice=int(input())

    if choice==1:
      print(add(m,n))
    elif choice==2:
        print(multiply(m,n))
    elif choice==3:
        result_m,result_n=subtract(m,n)
        print(result_m)
        print(result_n)

main()
'''


def swap(arr):
    arr[2], arr[3] = arr[3], arr[2]

def main():
    number =[10,20,30,40]
    print("Before swap:",number [2],",",number[3])
    swap(number)
    print("After swap:",number[2],",",number[3])

main()