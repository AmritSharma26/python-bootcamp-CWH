sentence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

count = 0
vowels = "aeiou"
# for vowel in vowels:
#     count += sentence.lower().count(vowel)

for char in sentence.lower():
    if char in vowels:
        count += 1

print(f"There are {count} vowels in the sentence")