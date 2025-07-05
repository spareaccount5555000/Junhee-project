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
        print(additionresult[i][j], end = " ")
    print("\n")

#SUBTRACTION RESULT
for i in range(2):
    for j in range(2):
        print(subtractionresult[i][j], end = " ")
    print("\n")