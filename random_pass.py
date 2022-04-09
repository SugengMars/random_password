import random 

password = int(input("masukan panjang password : "))

s="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

p = "".join(random.sample(s,password))
print(p)