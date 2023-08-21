def create_matrix(key):
    key = key.upper()
    matrix = [[0 for i in range (5)] for j in range(5)]
    letters_added = []
    row = 0
    col = 0
    for letter in key:
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
        if (col==4):
            col = 0
            row += 1
        else:
            col += 1
    for letter in range(65,91):
        # I/J
        if letter==74: 
                continue
        if chr(letter) not in letters_added:
            letters_added.append(chr(letter))
            
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index+=1
    return matrix

def separate_same_letters(plaintext):
    index = 0
    while (index<len(plaintext)):
        l1 = plaintext[index]
        if index == len(plaintext)-1:
            plaintext = plaintext + 'X'
            index += 2
            continue
        l2 = plaintext[index+1]
        if l1==l2:
            plaintext = plaintext[:index+1] + "X" + plaintext[index+1:]
        index +=2   
    return plaintext

def index(letter,matrix):
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            return (i,index)
        except:
            continue

def encrypt(key, plaintext):
    inc = 1
    matrix = create_matrix(key)
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(' ','')    
    plaintext = separate_same_letters(plaintext)
    encrypted_text=''
    for (l1, l2) in zip(plaintext[0::2], plaintext[1::2]):
        row1,col1 = index(l1,matrix)
        row2,col2 = index(l2,matrix)
        if row1==row2: 
            encrypted_text += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
        elif col1==col2:
            encrypted_text += matrix[(row1+inc)%5][col1] + matrix[(row2+inc)%5][col2]
        else: 
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    
    return encrypted_text

print(encrypt('HELLO', 'PLAYFAIR'))
