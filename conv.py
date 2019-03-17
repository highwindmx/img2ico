from PIL import Image
filename = 'demo.png'
img = Image.open(filename)
img.save('logo.ico')