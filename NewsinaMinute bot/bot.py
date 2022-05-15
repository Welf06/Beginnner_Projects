import discord
import os

client = discord.Client()
articles = []

@client.event 
async def on_ready():
   print(f"WE have logged in as {client.user}")
 

@client.event
async def on_message(message):
   if message.author == client.user:
      return
   
   if message.content.startswith("#hello"):
      await message.channel.send('Hello!')
   
   if message.content.startswith("#news"):
      articles.clear()
      import hindu_scrapper
      article_list = hindu_scrapper.article_list
      count = 0
      for i in list(article_list.keys()) :
         if message.content.lower()[6:] in i.lower():
            await message.channel.send(f"{count+1}. {i}")
            articles.append(article_list[i])
            count += 1
      
   if message.content.startswith("#article"):
      if len(articles) == 0:
         await message.channel.send("No headlines generated, please use #news to generate them")
      else:
         try:
            index= int(message.content[9:])
            try:
               await message.channel.send(articles[index-1][0:1999])
            except:
               await message.channel.send("The number is given is out of range of headlines generated")
         except:
            await message.channel.send("Please enter a valid Integer!")


client.run('OTQ2MzM2NDM2MjA5MjEzNTAw.YhdOfA.KVgfmIO-4OQ1OA3tyLMOsHn2Suw')

