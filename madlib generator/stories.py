def story1():
   while True:
      gender = input('Boy or Girl:  ')
      if gender.lower().strip() == 'boy':
         pronoun = 'his'
         break
      elif gender.lower().strip() == 'girl':
         pronoun = 'her'
         break
      else:
         print('Please choose from boy or girl')
   name = input(f'Enter {pronoun} name:  ').capitalize()
   colour1 = input('Enter 1st colour:  ')
   colour2 = input('Enter 2nd colour:  ')
   colour3 = input('Enter 3rd(and last:D) :  ')
   adjective = input('Enter an adjective:  ')
   room = input('Enter a room in the house:  ')
   number1 = input('Enter a number:  ')
   number2 = input('Enter another number:  ')
   time = input('Enter duration of time:  ')
   print(f'{name} closed the big {colour1} book. It slammed shut with a {adjective} bang, and a huge cloud of dust came from the old pages. {name} put the book back into the bookcase in the {room}, next to {number1} copy of Lord of the Rings, the best ever written. As {name} went to bed he smiled at the book and said, "I wish that I could fish!"')
   print(f'When he woke up after {time}, the magic book had granted his wish, and a {colour2} fishing rod and a {colour3} Bucket were next to his bed. {name} hugged the old {colour1} book, and {number2} seagulls flew into the window, to show him where to go fishing. ')

def story2():
   
    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    print('Last night I dreamed I was a ' +adjactive+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')

def story3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')
   
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')  
