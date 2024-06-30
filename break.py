'''
multiples=[]
for i in range(1,6+1):
    if i==4:
      break
    multiples.append(6*i)
print("The first five multiples of are:",multiples)
'''


'''
# only e enter then program in break then output print
print("Press any key or E to exit:")
while True:
    key = input()

    if key.lower()=='e':
        break
print("Goodbye!")
'''

'''
sum=0
i=1
n=int(input("Enter the n value:-"))

while i<n:
    number=int(input("Enter a number:-"))

    if number<2:
        break
    
    sum+=number
    i+=1
print("sum=",sum)
'''
'''
for i in range(1,4):
    for j in range(4):
        if i==2 and j==2:
            break #pass main print condition 
        print(i,j)
'''

