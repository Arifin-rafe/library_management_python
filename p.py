import hashlib
mm=input('put something : ')
password = mm.encode('utf-8')
hash_object = hashlib.sha256(password) 
hex_dig = hash_object.hexdigest()
print("my pass : ",hex_dig)