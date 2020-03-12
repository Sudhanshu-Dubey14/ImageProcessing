import sys
from PIL import Image, ImageOps
#import PIL
'''
img1 = sys.argv[1]
img2 = sys.argv[2]
img3 = sys.argv[3]
colour = sys.argv[4]

5
img1 = input("Enter 1st image: ")
img2 = input("Enter 2nd image: ")
img3 = input("Enter 3rd image: ")
'''


#colour = input("Enter the colour (out of red/blue/green) which you want to remove: ")
img = Image.open(sys.argv[1])
'''
image_data = image.load()

height,width = image.size

for loop1 in range(height):
	for loop2 in range(width):
		r,g,b = image_data[loop1,loop2]
		if image_data[loop1,loop2] != r:
			image_data[loop1,loop2] = 0,0,0

#image.save('final_output.jpeg')
#image = ImageOps.posterize(image,2)

image.show()
'''
pixels = img.load() # create the pixel map

for i in range(img.size[0]): # for every pixel:
	for j in range(img.size[1]):
		if pixels[i,j] <= (110, 0,0): # or pixels[i,j] != (255,255,255):
		# change to black if not red
			pixels[i,j] = (0, 0 ,0)
	

img.save('final_output.jpeg')
