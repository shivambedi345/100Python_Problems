A=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
B=[
    [9,8,7,11],
    [6,5,4,12],
    [3,2,1,13]
    ]
result=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]
for r in result:
    print(r)
