from PIL import Image
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

def get_img_matrix(img):
   width, height = img.size
   # resizing image to fit in terminal
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
   ascii_matrix = get_ascii_matrix(img)
   for row in range(len(ascii_matrix)):
      for column in ascii_matrix[row]:
         print(column*3, end = ' ')
      print()
def img_resize(img):
   basewidth = 300
   wpercent = (basewidth/float(img.size[0]))
   hsize = int((float(img.size[1])*float(wpercent)))
   img = img.resize((basewidth,hsize), Image.ANTIALIAS)
   display_ascii_art(img)
 

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
image = Image.open(filename)

#to check whether wifth>300 to resize
if image.size[0] >300:
   img_resize(image)
else :
   display_ascii_art(image)

      
      
   

      



