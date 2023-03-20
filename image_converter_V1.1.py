from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Import ttk for progress bar

def browse_input_folder():
    folder = filedialog.askdirectory()
    input_folder_var.set(folder)

def browse_output_folder():
    folder = filedialog.askdirectory()
    output_folder_var.set(folder)

def update_output_folder_visibility(*args):
    if output_option_var.get() == "Choose folder":
        output_folder_entry.grid(row=2, column=1)
        browse_output_folder_button.grid(row=2, column=2)
    else:
        output_folder_entry.grid_remove()
        browse_output_folder_button.grid_remove()

def convert_images():
    image_path = input_folder_var.get()
    output_option = output_option_var.get()
    new_name = new_name_var.get()
    conversion_type = conversion_type_var.get()
    change_name = change_name_var.get()
    conversion_method = conversion_method_var.get()

    if not image_path:
        messagebox.showerror("Error", "Please select an input folder.")
        return

    if output_option == "Choose folder":
        output_path = output_folder_var.get()
        if not output_path:
            messagebox.showerror("Error", "Please select an output folder.")
            return
    else:
        output_path = image_path

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    images = os.listdir(image_path)
    num = 1

    # Set progress bar maximum value
    progress_bar["maximum"] = len(images)
    progress_bar["value"] = 0

    for i in images:
        input_file = os.path.join(image_path, i)
        im = Image.open(input_file)
        con_im = im.convert(conversion_method)

        if change_name:
            output_file = os.path.join(output_path, new_name + "_" + str(num) + conversion_type)
            num += 1
        else:
            original_name = os.path.splitext(i)[0]
            output_file = os.path.join(output_path, original_name + conversion_type)

        con_im.save(output_file)

        # Update progress bar
        progress_bar["value"] = num
        root.update_idletasks()
        num += 1

    messagebox.showinfo("Success", "Conversion completed!")

root = tk.Tk()
root.title("Image Converter")

input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
output_option_var = tk.StringVar()
new_name_var = tk.StringVar()
conversion_type_var = tk.StringVar()
change_name_var = tk.BooleanVar()
conversion_method_var = tk.StringVar()

tk.Label(root, text="Input folder:").grid(row=0, column=0, sticky="e")
input_folder_entry = tk.Entry(root, textvariable=input_folder_var, width=50)
input_folder_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_input_folder).grid(row=0, column=2)

tk.Label(root, text="Output option:").grid(row=1, column=0, sticky="e")
output_option_options = ["Choose folder", "Convert in place"]
output_option_dropdown = tk.OptionMenu(root, output_option_var, *output_option_options)
output_option_var.set(output_option_options[0])
output_option_dropdown.grid(row=1, column=1, sticky="w")

output_option_var.trace('w', update_output_folder_visibility)

tk.Label(root, text="Output folder:").grid(row=2, column=0, sticky="e")
output_folder_entry = tk.Entry(root, textvariable=output_folder_var, width=50)
output_folder_entry.grid(row=2, column=1)
tk.Button(root, text="Browse", command=browse_output_folder).grid(row=2, column=2)

tk.Label(root, text="Conversion type:").grid(row=3, column=0, sticky="e")
conversion_type_options = [".jpg", ".png", ".tga"]
conversion_type_dropdown = tk.OptionMenu(root, conversion_type_var, *conversion_type_options)
conversion_type_var.set(conversion_type_options[0])
conversion_type_dropdown.grid(row=3, column=1, sticky="w")

tk.Label(root, text="Conversion method:").grid(row=4, column=0, sticky="e")
conversion_method_options = ["RGBA", "RGB", "L", "P", "1"]
conversion_method_dropdown = tk.OptionMenu(root, conversion_method_var, *conversion_method_options)
conversion_method_var.set(conversion_method_options[0])
conversion_method_dropdown.grid(row=4, column=1, sticky="w")

tk.Label(root, text="Change name:").grid(row=5, column=0, sticky="e")
change_name_checkbox = tk.Checkbutton(root, variable=change_name_var)
change_name_checkbox.grid(row=5, column=1, sticky="w")

tk.Label(root, text="New name:").grid(row=6, column=0, sticky="e")
new_name_entry = tk.Entry(root, textvariable=new_name_var)
new_name_entry.grid(row=6, column=1)

tk.Button(root, text="Convert", command=convert_images).grid(row=7, column=1, pady=10)

# Add progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.grid(row=8, column=1, pady=5)

root.mainloop()

