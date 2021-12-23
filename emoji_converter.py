word = input('>').split()
emojis = {
   ':)' : '😊',
   ':(' : '😥',
   ':D' : '😄'
}
for i in word:
   print(emojis.get(i, i), end = ' ')

