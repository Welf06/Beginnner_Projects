import imp
from math import pi
print("FINDING Nth DIGIT OF PI")
try:
   num = int(input("N = "))
except:
   print("Enter a valid integer!")

if num > 48 or num < 0:
   print("Please enter a num between 0 to 48")
else:
   print(f"{pi:.48f}"[num+1])