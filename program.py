import sys
from PIL import Image
'''
img1 = sys.argv[1]
img2 = sys.argv[2]
img3 = sys.argv[3]
colour = sys.argv[4]
'''

img1 = input("Enter 1st image: ")
img2 = input("Enter 2nd image: ")
img3 = input("Enter 3rd image: ")

colour = input("Enter the colour (out of red/blue/green) which you want to remove: ")

images = [Image.open(x) for x in [img1, img2, img3]]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('output.jpg')

image = Image.open('output.jpg')

image_data = image.load()

height,width = image.size

for loop1 in range(height):
	for loop2 in range(width):
		r,g,b = image_data[loop1,loop2]
		if colour == 'red':
			image_data[loop1,loop2] = 0,g,b
		elif colour == 'blue':
			image_data[loop1,loop2] = r,g,0
		elif colour == 'green':
			image_data[loop1,loop2] = r,0,b

image.save('final_output.jpeg')
