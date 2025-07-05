#matrix  =  [[1,2,3],[4,5,6],[7,8,9]]
#print(len(matrix))
#print(len(matrix[0]))
#print(matrix[1][2])
#for i in range(0,len(matrix)):
    #for j in range(0,len(matrix[0])):
        #print(matrix[i][j], end="")
    #print("\n")



#rows = int(input("Enter the number of rows - "))
#columns = int(input("Enter the numbeer of columns - "))
#matrix = []

#for i in range(rows):
    #temp = []
    #for j in range(columns):
        #x = int(input("Enter your element - "))
        #temp.append(x)
    #matrix.append(temp)

#for i in range(rows):
    #for j in range(columns):
        #print(matrix[i][j])
    #print("\n")



#matrix2 = []

#n = int(input("Enter the dimentions of the matrix - "))

#for i in range(n):
    #temp = []
    #for i in range(n):
        #x = int(input("Enter your element - "))
        #temp.append(x)
    #matrix2.append(temp)

#for i in range(n):
    #print(matrix2[i][i])




matrixA = [[1,2],[3,4]]
matrixB = [[5,6],[7,8]]

additionresult = [[0,0],[0,0]]
subtractionresult = [[0,0],[0,0]]

for i in range(0,2):
    for j in range(0,2):
        additionresult[i][j] = matrixA[i][j] + matrixB[i][j]
        subtractionresult[i][j] = matrixA[i][j] - matrixB[i][j]

#ADDITION RESULT
for i in range(2):
    for j in range(2):
        print(additionresult[i][j], end = "")
    print("\n")

#SUBTRACTION RESULT
for i in range(2):
    for j in range(2):
        print(subtractionresult[i][j], end = "")
    print("\n")

