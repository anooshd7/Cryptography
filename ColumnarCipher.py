import math
key = "ZEBRAS"

def encrypt(plaintext):
    encrypted_text = ""
    k = 0
    string_len = len(plaintext)
    l1 = list(plaintext)
    l2 = sorted(list(key))
  
    col = len(key)
    row = int(math.ceil(string_len / col))
  
    fill_spaces = int((row * col) - string_len)
    l1.extend('x' * fill_spaces)

    matrix = [l1[i: i + col] for i in range(0, len(l1), col)]

    for i in range(col):
        current_index = key.index(l2[k])
        encrypted_text += ''.join([row[current_index] for row in matrix])
        k += 1
  
    return encrypted_text

print(encrypt('HELLOWORLDPYTHON'))