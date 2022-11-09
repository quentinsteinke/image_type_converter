from PIL import Image
import os

image_path = ".\\convert\\"
new_name = "Converted_Image"
make_converted_dir = "no value set"
conversion_method = "RGB"
conversion_type = ".jpg"

# See if you need forward-slash or back-slash for you os
try:
    images = os.listdir(image_path)
    print("windows os")
    try:
        make_converted_dir = ".\\converted\\"
        os.makedirs("converted")
        print("making converted folder")
        print("Converting " + str(len(images)) + " images", images)
    except FileExistsError:
        print("Converted folder already exists")

except FileNotFoundError:
    image_path = "./convert/"
    images = os.listdir(image_path)
    print("linux os")
    make_converted_dir = "./converted/"
    try:
        os.makedirs("converted")
        print("makeing converted")
    except FileExistsError:
        print("Converted folder already exists")

except:
    print("No 'convert' folder found")

while True:
    print("Converting " + str(len(images)) + " images")
    for i in images:
        print(i)
    print("Convert to: (1)jpg (2)png (3)tga")

    selection = input()

    try:
        selection = int(selection)
    except ValueError:
        pass

    if selection == 1:
        conversion_type = ".jpg"
        break
    elif selection == 2:
        conversion_type = ".png"
        break
    elif selection == 3:
        conversion_type = ".tga"
        break
    else:
        error_string = (str(selection) + ", is not a valid answer")
        error_border = ""
        print(error_string)
        length = len(error_string)
        while length > 0:
            error_border += "-"
            length -= 1
        print(error_border)

while True:
    print("Change name? y/n: ")
    convert_name = input()
    error_border = ""

    if convert_name == "y" or convert_name == "n":
        break
    else:
        error_string = (str(convert_name) + ", is not a valid answer")
        print(error_string)
        length = len(error_string)
        while length > 0:
            error_border += "-"
            length -= 1
        print(error_border)


if convert_name == "y":
    print("New file name: ")
    new_name = input()
    num = 1

    for i in images:
        i = image_path + i
        im = Image.open(i)
        con_im = im.convert(conversion_method)
        con_im.save(make_converted_dir + new_name + "_" + str(num) + conversion_type)
        num += 1

if convert_name == "n":
    image_sufix = [".png", ".jpg", ".tif", ".tga", ".TGA"]

    for i in images:
        i = image_path + i
        im = Image.open(i)
        original_name = im.filename
        original_name = original_name.replace(image_path, "")

        for i in image_sufix:
            original_name = original_name.replace(i, "")

        con_im = im.convert(conversion_method)
        print(original_name + str(conversion_type))
        con_im.save(make_converted_dir + original_name + str(conversion_type))

print("All done!")
