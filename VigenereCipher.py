def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encryption(string, key): 
  encrypted_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    encrypted_text.append(chr(x)) 
  return("" . join(encrypted_text)) 

def decryption(encrypt_text, key): 
  original_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    original_text.append(chr(x)) 
  return("" . join(original_text)) 

key = generateKey('HELLO', 'abcd')
encrypted_text = encryption('HELLO', key)
print("Encrypted message: ", encrypted_text) 
print("Decrypted message: ", decryption(encrypted_text, key)) 