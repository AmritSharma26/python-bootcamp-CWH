password = "password123"
user_input = ""

while password != user_input:
    user_input = input("Enter the password: ")
    if(password != user_input):
        print("Incorrect Password!!")
    else:
        print("Success!")