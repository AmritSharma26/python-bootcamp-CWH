# Part 1
import math

print("Square root of 144:", math.sqrt(144))
print("sin(90) =", math.sin(math.radians(90)))

# Part 2
import requests

data = requests.get("https://api.github.com")
print(data.json())