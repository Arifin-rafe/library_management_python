import hashlib
user_password = input ("Enter user password : ")
encode_user_password = user_password.encode('utf-8')
hashed = hashlib.sha256(encode_user_password)
hashed_password_digit = hashed.hexdigest()
print(hashed_password_digit)