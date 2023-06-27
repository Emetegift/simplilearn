#This will simply print all the values in in x, because i has bn iterated on th values of x
# x = [1,2,3,4,5,6,]
# for i in x:
#     print(i)

# ##
# x = [(1,2,3,4,5,),'sup', (12,22,23)]
# for i in x :
#     for j in i :
#      print(j, end='') #the end='' will make everything to be printed on a single line 





# # to print a range of numbers
# for i in range(0,21):
#     print(i)




# # to find teh sum of even numbers in a range of numbers
# sum =0
# for i in range(0,21):
#     if i%2==0:
#         sum = sum+i
#         print(sum)
        

# To print patterns by taking input from the user
# n = int(input("Enter a number"))
# for i in range(1, n+1):
#     for j in range(1, i+1):  ##Exmple of a nsted for loop
#         print(j, end='')
#     print()
    
    
## Nested For loop for accesing the elements of a matrix as a list containing lists

r = int(input("Enter number of rows"))
c = int(input("Enter number of columns"))
 # create our first list 
x =[]
val =[]
 # to iterat over the element in x
for i in range(0, r):  # for r is the number of elements in x and c is the number of elent in the list in x
    for j in range(0, c) :
        val.insert(j, int(input("Enter the %d * %d element" %(i, j)))) # inside list
   
    x.insert(i, val)    # ADD the list val to the main list, x which is the parent list
    val=[] 

y=[]
for i in range(0, r):  # for r is the number of elements in x and c is the number of elent in the list in x
    for j in range(0, c) :
        val.insert(j, int(input("Enter the %d * %d element" %(i, j))))
   
    y.insert(i, val) 
    val=[]

# To find the sum for the two list
sum = []
# to access a list containing lists

for i in range(0, r):
    for j in range(0, c):
        val.insert(j, x[i][j]+ y[i][j])
    sum.insert(i, val)
    val=[]
print(sum)
    
    
    
    
    
    
    
    
    
    
