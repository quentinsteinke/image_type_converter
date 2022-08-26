from PIL import Image
import os

image_path = ".\\convert\\"
new_name = "Converted_Image"
make_converted_dir = "no value set"
conversion_type = "RGB"

# See if you need forward-slash or back-slash for you os
try:
    images = os.listdir(image_path)
    make_converted_dir = ".\\converted\\"
except FileNotFoundError:
    image_path = "./convert/"
    images = os.listdir(image_path)
    make_converted_dir = "./converted/"
    print("Converting " + str(len(images)) + " images", images)
else:
    print("No 'convert' folder found")

print("Change name? y/n: ")
convert_name = input()

try:
    os.makedirs("converted")
except FileExistsError:
    pass


if convert_name == "y":
    print("New file name: ")
    new_name = input()
    num = 1

    for i in images:
        i = image_path + i
        im = Image.open(i)
        con_im = im.convert(conversion_type)
        con_im.save(make_converted_dir + new_name + "_" + str(num) + ".jpg")
        num += 1

if convert_name == "n":
    for i in images:
        i = image_path + i
        im = Image.open(i)
        original_name = im.filename
        original_name = original_name.replace(image_path, "")
        original_name = original_name.replace(".png", "")
        con_im = im.convert(conversion_type)
        print(make_converted_dir)
        con_im.save(make_converted_dir + original_name + ".jpg")

print("All done!")
