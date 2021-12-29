from PIL import Image
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

def get_img_matrix(img):
   
   """(Image) -> list of list of tuple\n
   Takes an image and converts it into a list of list containing (r,g,b) of each pixel of each row
   """
   
   width, height = img.size
   
   # resizing image as the aspect ratio of a 
   # charecter in the terminal is a rectangle compared to the square of pixel
   img.resize((width//2, height//2))
   
   # initializing a list to store the rgb of each pixel of a row in a 2D array for the whole image
   image_list = []
   pxl = img.load()

   for y in range(height):
      row = []
      for x in range(width):
         row.append(pxl[x,y])
      image_list.append(row)
      
   return image_list

def get_brightness_matrix(img):
   """(Image) -> list of list of int\n
   Takes an image and converts it into a list of list containing brightness of each pixel of each row
   """
   
   image_matrix = get_img_matrix(img)
   brightness_list = []
   
   for rows in range(len(image_matrix)):
      row = []
      for column in image_matrix[rows]:
         r,g,b = column
         average = (r+g+b)//3
         row.append(average)
      brightness_list.append(row)
      
   return brightness_list

def get_ascii_matrix(img):
   
   """(Image) -> list of list of str\n
   Takes an image and converts it into a list of list containing a string which maps to brightness
   of each pixel of each row
   """
   
   ascii_map = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
   brightness_matrix = get_brightness_matrix(img)
   ascii_matrix = []
   
   for rows in range(len(brightness_matrix)):
      row = []
      for column in brightness_matrix[rows]:
         map_index = column//4
         row.append(ascii_map[map_index])
      ascii_matrix.append(row)
      
   return ascii_matrix

def display_ascii_art(img):
   
   """(Image) -> str\n
   Takes an image and converts it into an ASCII art and prints it
   """
   
   ascii_matrix = get_ascii_matrix(img)
   for row in range(len(ascii_matrix)):
      for column in ascii_matrix[row]:
         print(column*3, end = ' ')
      print()
      
def img_resize(img):
   
   """(Image) -> string\n
   Resizes the image to a width of 300 pixels and height, maintaining the aspect ratio
   """
   
   basewidth = 300
   widthpercent = (basewidth/float(img.size[0]))
   hsize = int((float(img.size[1])*float(widthpercent)))
   img = img.resize((basewidth,hsize), Image.ANTIALIAS)
   display_ascii_art(img)
 
 
# to take input from user using gui of the os
Tk().withdraw() 
filename = askopenfilename()
image = Image.open(filename)

#to check whether wifth>300 to resize
if image.size[0] >300:
   img_resize(image)
else :
   display_ascii_art(image)

      
      
   

      




