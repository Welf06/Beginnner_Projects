# converting given weight from kg to lbs or vice versa
print("Enter your weight:")
weight = int(input())
unit = input('lbs or kg: ').strip().lower()
if unit == 'kg':
   print(f'Your weight in pounds: {(weight*2.20462):.1f}lbs')
elif unit == 'lbs':
   print(f'Your weight in kilograms: {(weight*0.453592):.1f}kg')
else:
   print('Enter a proper unit!')