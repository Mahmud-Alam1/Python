#decimal to binary number?
n=int(input("Enter a decimal number:"))
l=list()
while n!=0:
    r=n%2
    l.append(r)
    n=n//2
l.reverse()
print(l)

'''
l=8
print(bin(l))
'''




