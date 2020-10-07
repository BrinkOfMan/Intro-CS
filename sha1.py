#SHA-1 cryptgraphic hash

import hashlib

#function to return the SHA-1 digest of a message
def SHA1(msg):
    s = hashlib.sha1()
    s.update(msg.encode())
    return s.hexdigest()


#prompt the user for a message and compute its SHA-1 digest
message = input("Enter a message: ")
print("The SHA-1 digest is:", SHA1(message))

