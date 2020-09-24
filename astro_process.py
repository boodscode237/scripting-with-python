from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
'''
	to save in a special file of your own,
	 you van create the path of the file you 
	 want to save your image to
	1-create the folder
	2create the path like on the next line and 
	add thge name you want plus the file type
 '''
pathfile = ('./saved_pics/')+'resized.jpg'
thumbnail = ('./saved_pics/')+'thumbnail.jpg'

# this will not keep the size ratio
new_img = img.resize((600,400))
new_img.save('thumbnail.jpg')

# this will kepp the size ratio
img.thumbnail((600,500))
img.save(thumbnail)

print(img.size)