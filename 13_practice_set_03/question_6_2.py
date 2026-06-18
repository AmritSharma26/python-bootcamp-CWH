str = input("Enter a string: ")
if str.lower() == str[::-1].lower():
    print("'"+str+"'", "is a palindrome")
else: 
    print("'"+str+"'", "is not a palindrome")