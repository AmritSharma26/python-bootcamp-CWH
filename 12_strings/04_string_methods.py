s = "hello world" # String are immutable

# s[0] = "R" # 'str' object does not support item assignment

a = len(s)
print(a)

# print(s.upper(), s)
# print(s.lower())
# print(s.capitalize())
# print(s.title())

# text = "  \nawesome world  "
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip()

# text = "Python is fun"
# print(text.find("is")) # index of first occurence
# print(text.replace("fun", "awesome")) # replace all occurence

# text = "Apples,Bananas,Pineapples"
# print(text.split(","))
# print(",".join(["Apples", "Bananas", "Pineapples"]))

text = "Python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())