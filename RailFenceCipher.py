def encrypt(text, key):
    matrix = []
    dir = False
    row, col = 0, 0
     
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir = not dir
        matrix[row][col] = text[i]
        col += 1
        if dir:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if matrix[i][j] != '\n':
                result.append(matrix[i][j])
    return("" . join(result))

print(encrypt('Hello World',3))