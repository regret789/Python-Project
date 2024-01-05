import random
letter=['a','b,''f']
symbol=['@','#','%','$']
number=['1','2','3','44']
print("Welcome to the password generator!")
n_letter=int(input("How many letter you want to include in generating password? "))
n_symbol=int(input("How many symbol you want to include in generating password?"))
n_number=int(input("How many number you want to include in generatng password? "))
password=""

for i in range(1,n_letter+1):
    char=random.choice(letter)
    password+=char

    for i in range(1,n_symbol+1):
        char=random.choice(symbol)
        password +=char

        for i in range(1,n_number+1):
            char=random.choice(number)
            password+=char

            print("password")