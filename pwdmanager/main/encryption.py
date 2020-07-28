from cryptography.fernet import Fernet
import base64

key = b'ylZalYY7uLxKI98Um5fpNlOJZs_CqHNoSR3yi9k7qlM='

# def encrypt(message, key):
#     cipher = Fernet(key)
#     message = message.encode('utf-8')
#     token = cipher.encrypt(message)
    
#     x = (token.decode('utf-8'))
#     #print(x)
#     return x

# def decrypt(key, token):
#     cipher = Fernet(key)

#     decoded = cipher.decrypt(token)
#     decoded = decoded.decode('utf-8')
#     #print(decoded)
#     return decoded

def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 

def decrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 