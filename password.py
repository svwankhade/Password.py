import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("Welcome to the Password Generator!")
l=int(input("How many letters would you like in your password ?\n"))
s=int(input("How many symbols would you like in your password ?\n"))
n=int(input("How many numberss would you like in your password ?\n"))
password=[]
for i in range(1,l+1):
    c=random.choice(letters)
    password.append(c)
for i in range(1,s+1):
    S=random.choice(symbols)
    password.append(S)
for i in range(1,n+1):
    I=random.choice(numbers)
    password.append(I)  
random.shuffle(password)
p = ""
for i in password:
    p = p +i 
print(f"Your password is: {p}")
 

