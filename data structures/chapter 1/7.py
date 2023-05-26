def set_to_0(m):
    rows = len(m)
    cols = len(m[0])
    flag = False
    for i in range(rows):
        for j in range(cols):
            if m[i][j] == 0:
                flag = True
                break
        if flag:
            break
    for x in range(cols):
        m[i][x] = 0
    for y in range(rows):
        m[y][y] = 0

    return m

mat = [[1,1,1],[0,2,3]]
print(mat)
print(set_to_0(mat))