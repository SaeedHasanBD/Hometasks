"""5. Написать программу, которая принимает от пользователя имя и пароль. Сравнивает пароль с заданным в коде.
	В случае совпадения печатает в консоль "Password for user: <Имя пользователя> is correct"
	Если пароль не совпадает, то печатает в консоль
	"Password for user: <Имя пользователя> is incorrect"
	"Please try again..."
	И снова запрашивает пароль (не завершается).
5. Write a program that accepts the user's name and password. Compares the password with the one specified in the code.
	In case of a match, prints "Password for user: <username> is correct" to the console"
	If the password does not match, it prints to the console
	"Password for user: <username> is incorrect"
	"Please try again..."
	And again asks for the password (not completed).
"""

mainpassword= "Hasan"

def password_matcher():
    username = input("Enter username: ")
    while True:
        password = input("Enter your password: ")
        if password == mainpassword:
            print("Password for user: {} is correct".format(username))
            break
        else:
            print("Password for user: {} is incorrect.\nPlease try again...".format(username))


password_matcher()



