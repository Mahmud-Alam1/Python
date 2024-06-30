'''
#write the 2-D Array
rows=int(input("Enter the number of row:-"))
cols=int(input("Enter the number of cols:-"))

arr=[[0 for j in range(cols)] for i in range(rows)]
#0<2      r---0<2
print("Enter the element of the array:")
for i in range(rows):                #0<2   #1<2   
    for j in range(cols):   #0<2     1<2     0<2   1<2
        arr[i][j]=int(input())   #0,0--10  0,1--20   1,0--30    1,1--40
print("the two-dimensional array is:")
for i in range(rows):
    for j in range(cols):
        print("({},{})".format(i, j), arr[i][j],end=" ")
    print()
'''

'''
#write the index of array
arr=[[1, 2], [3, 4], [5, 6]]
for i in range(0,3):
    for j in range(0,2):
        print("({},{})".format(i, j), arr[i][j],end=" ")
    print()
'''

'''
#write the sum od digonal array
a=[[1,2,3],
  [4,5,6],
   [7,8,9]]
sum=0
for i in range(len(a)):   #    2<3---R 
    for j in range(len(a)):   # 3<3  --- COLN 

#[0,0 =1  0,1=2    0,2 =3    ]
#[1,0=4  1,1=5     1,2=6]
#[2,0=7  2,1=8      2,2=9]
        if i==j:
            sum=sum+a[i][j]  # 0+1=1+5=6+9=15
print(sum)# 15

#   1   2   3
#   4   5   6
#   7   8   9
'''


#sum of total matrix
arr=[[1,2],[3,4],[5,6]]
total_sum=0
for i in range(0, 3):
    for j in range(0, 2): 

        total_sum+=arr[i][j] 
        print("Element at row:", i, "and column:", j, "is:", arr[i][j])     # 00-1 0+1=1, 01-2  1+2=3
print("sum of al elements in the matrix:",total_sum)