from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))


filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png",'png')


filtered_img1 = img.filter(ImageFilter.BLUR)
filtered_img1.save("blur.png",'png')


filtered_img2 = img.filter(ImageFilter.SHARPEN)
filtered_img2.save("sharpen.png",'png')

# transform the image to black and white
convert_img = img.convert('L')
convert_img.save('grey.png','png')



crooked = filtered_img.rotate(180)
crooked.save("rotated.png",'png')

# filtered_img.show()

resized = filtered_img.resize((300, 300))
resized.save("resized.png",'png')

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("region.png",'png')