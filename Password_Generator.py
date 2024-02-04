import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
         'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
         'Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*']
print("Hello, Welcome to the Password Generator!!")
length=int(input("Enter the length of the password you want: \t"))
n_letters=int(input("Enter how many letters you want: \t"))
n_numbers=int(input("Enter how many numbers you want: \t"))
n_symbols=int(input("Enter how many symbols you want: \t"))
total_length=(n_letters)+(n_numbers)+(n_symbols)
password_list=[]
if length==total_length:
    for i in range(1,n_letters+1):
        char = random.choice(letters)
        password_list+=char
    for i in range(1,n_numbers+1):
        char=random.choice(numbers)
        password_list+=char
    for i in range(1,n_symbols+1):
        char=random.choice(symbols)
        password_list+=char
    random.shuffle(password_list)
    print("".join(password_list))
else:
    print("The Total Characters length should have to match with your Password length")



