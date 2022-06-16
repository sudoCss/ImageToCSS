# Imports ssss
from PIL import Image
from os import path
from sys import argv

# Parsing passed args
img_path = argv[1]

# Validating the passed image path
if not img_path.endswith('.jpg') and not img_path.endswith('.png') and not img_path.endswith('.jpeg'):
  print('Not valid image!') 
  exit()

if not path.exists(img_path):
  print('Image not exist!')
  exit()

img_file = Image.open(img_path)

# Scaling the image to 64 px height while saving 
# the aspact ratio and save the new scaled to resized_nearest.jpg
fixed_height = 64
height_percent = (fixed_height / float(img_file.size[1]))
width_size = int((float(img_file.size[0]) * float(height_percent)))
image = img_file.resize((width_size, fixed_height), Image.NEAREST)
image.save('resized_nearest.jpg')
img_file.close()

# Create new html file and add some initial stuff
# w to create new file and delete the old if exists
file = open("index.html", "w")
file.write("<!DOCTYPE html>\n\
<html lang=\"en\">\n\
<head>\n\
    <meta charset=\"UTF-8\">\n\
    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\
    <title>PIC</title>\n\
    <style>")
file.close()

# Add some initial CSS, a to append to the file
file = open("index.html", "a")
file.write("* {\n\
  margin: 0;\n\
  box-sizing: border-box;\n\
}\n\
\n\
.pic {\n\
  width: 0px;\n\
  height: 0px;\n\
  box-shadow:\n")

# Open the resized image and load pixels
scaled_img_file = Image.open("resized_nearest.jpg")
pix = scaled_img_file.load()
pixel_size = 4

# Adding pixels from the image to the css style with box-shadow
for i in range(1, scaled_img_file.height):
    for j in range(1, scaled_img_file.width):
        if (i == (scaled_img_file.height - 1)) and (j == (scaled_img_file.width - 1)):
             file.write("    " + str((j - 1) * pixel_size) + "px " + str((i - 1) * pixel_size) + "px 0 " + str(pixel_size) + "px rgb" + str(pix[j, i]) + ";\n  }\n") 
        else:
            file.write("    " + str((j - 1) * pixel_size) + "px " + str((i - 1) * pixel_size) + "px 0 " + str(pixel_size) + "px rgb" + str(pix[j, i]) + ",\n")

# Closing files
file.write("</style>\n\
</head>\n\
<body>\n\
    <div class=\"pic\"></div>\n\
</body>\n\
</html>")

scaled_img_file.close()
file.close()

