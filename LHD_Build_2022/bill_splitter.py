print("BILL SPLITTER\n")
try:
   print("Enter the total bill amount: ")
   bill = int(input())
   print("Enter the number of people splitting the bill:")
   people = int(input())
   print("Each person has to pay:", round(bill/people))
except:
   print("Please enter a valid number")
   