# Lab 1 
# Ceasar Cipher, Vigenere Cipher, Play fair cipher, Rail fence cipher, Columnar cipher

def CeasarCipher(original, key):
    result = ""
    for i in range(len(original)):
        c = original[i]
        if c.isupper():
            result += chr((ord(c) + key- 65) % 26 + 65)
        else:
            result += chr((ord(c) + key - 97) % 26 + 97)
            
    return result
CeasarEncrypted = CeasarCipher('hello', 3)
print("Encrypted text: " + CeasarEncrypted)
# For Decrypted, new key = 26 - original key
CeasarDecrypted = CeasarCipher(CeasarEncrypted, 23)
print("Decrypted text: " + CeasarDecrypted)
    



    
            
    




