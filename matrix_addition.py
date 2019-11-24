matrix = []
matrix1 = matrix.copy()
matrix2 = matrix.copy()
rows, cols = input("Enter the size of matrix: ").split(",")

for row in range(int(rows)):
    matrix1.append(input("Enter the row values: ").split(","))

for row in range(int(rows)):
    matrix2.append(input("Enter the row values: ").split(","))

for i in range(0, int(rows)):
    _ = []
    for j in range(0, int(cols)):
        _.append(int(matrix1[i][j]) + int(matrix2[i][j]))
    matrix.append(_)

for i in range(0, int(rows)):
    for j in range(0, int(cols)):
        print(matrix[i][j], end="    ")
    print()



#Output
# Enter the size of matrix: 3,3
# Enter the row values: 1,2,3
# Enter the row values: 2,3,1
# Enter the row values: 3,2,1
# Enter the row values: 3,2,1
# Enter the row values: 2,3,1
# Enter the row values: 1,2,3
# 4    4    4    
# 4    6    2    
# 4    4    4    
