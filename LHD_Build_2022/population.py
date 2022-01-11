import csv

print("""
      WELCOME TO COUNTRY POPULATION FINDER
      
   Please enter any country's name to get its info""")
country = input("  ").title()
with open("World Population.csv") as population:
   csv_reader = csv.reader(population)
   next(csv_reader)
   for line in csv_reader:
      if country in line[1]:
         print(f"""
   country:   {line[1]}
   rank:      {line[0]}
   continent: {line[2]}
   popolation:{line[3]}
               """)