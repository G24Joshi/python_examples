# Example: add two matrices using list comprehension

X = [[12,9,3],
    [4,5,6],
    [7,8,3]]

Y = [[9,8,1],
    [6,7,3],
    [4,5,9]]

result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)
