from posixpath import splitext
import sys
import os.path
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

allowed_formats = ['.jpg', '.jpeg', '.png']

input_file_extension = splitext(input_file_name)[1]
output_file_extension = splitext(output_file_name)[1]

if input_file_extension not in allowed_formats:
    sys.exit('Invalid input')

if output_file_extension not in allowed_formats:
    sys.exit('Invalid output')

if input_file_extension.lower() != output_file_extension.lower():
    sys.exit('Input and output have different extensions')

if not os.path.isfile(input_file_name):
    sys.exit('File does not exist')


image_file = Image.open(input_file_name)
shirt_file = Image.open('shirt.png')

size = shirt_file.size
muppet = ImageOps.fit(image_file, size)
muppet.paste(shirt_file, shirt_file)

muppet.save(output_file_name)