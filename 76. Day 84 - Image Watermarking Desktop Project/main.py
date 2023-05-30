import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog

from PIL import Image

FONT = ('times', 18, 'bold')
FONT_2 = ('times', 7, 'bold')

window = tk.Tk()
window.geometry("800x800")  # Size of the window
window.title('www.plus2net.com')

# count = 0

# Heading
select_image_label = tk.Label(window, text='Select Image', width=30, font=FONT)
select_image_label.grid(row=1, column=1)

# Add Watermark Button
add_watermark_button = tk.Button(window, text='Upload Watermark',
                                 width=20, command=lambda: upload_watermark())
add_watermark_button.grid(row=2, column=2)

# Upload Images Button
upload_image_button = tk.Button(window, text='Upload Files',
                                width=20, command=lambda: non_watermark_images())
upload_image_button.grid(row=3, column=0)

# File Format Button Dropdown
menu = StringVar()
menu.set("Select File Format")

file_format = OptionMenu(window, menu, 'PNG', 'JPEG')
file_format.grid(row=5, column=1)

# Location of the Button Entry
location_label = tk.Label(window, text='Location', font=FONT_2)
location_label.place(x=280, y=120)

location_dropdown = tk.Entry(window, width=20)
location_dropdown.place(x=330, y=120)

# Size of the Watermark Entry
size_label = tk.Label(window, text='Width x Height', font=FONT_2)
size_label.place(x=550, y=80)
# size_label.place(x=130, y=150)

width_entry = tk.Entry(window, width=5)
width_entry.place(x=620, y=80)

x_label = tk.Label(window, text="x", font=FONT_2)
x_label.place(x=660, y=80)

height_entry = tk.Entry(window, width=5)
height_entry.place(x=680, y=80)

# Transparency of the Watermark Entry
transparency_label = tk.Label(window, text='Opacity', font=FONT_2)
transparency_label.place(x=550, y=110)
# transparency_label.place(x=130, y=180)

transparency_entry = tk.Entry(window, width=5)
transparency_entry.place(x=620, y=110)

percent_label = tk.Label(window, text="%", font=FONT_2)
percent_label.place(x=660, y=110)

# Add Watermark Button
add_watermark = tk.Button(window, text='Add Watermark',
                          width=20, command=lambda: add_watermark_to_images())
add_watermark.place(x=0, y=100)

# Edit Watermark Button
edit_watermark = tk.Button(window, text='Edit Watermark',
                           width=20, command=lambda: edit_watermark())
edit_watermark.place(x=575, y=140)

# Error label
error_label = tk.Label(window, text='', font=FONT, fg='red')
error_label.place(x=270, y=250)

filenames_watermark = ""
filename_edit_watermark = ""
watermark = ""


def save_file(img, filename, x, location_result, file_format_result):
    """Save Pillow Image at a location"""
    if location_result is not None:
        x = location_result

    temp1 = x.split('/')[-1].split('.')[-2]
    try:
        open('/'.join(x.split("/")[:-1]) + f"/{filename}/", 'r')
    except FileNotFoundError:
        os.mkdir('/'.join(x.split("/")[:-1]) + f"/{filename}/")
    except PermissionError:
        pass

    print(file_format_result)
    save_filename = '/'.join(x.split("/")[:-1]) + f"/{filename}/" + temp1 + f"_watermarked.{file_format_result.lower()}"
    # print(save_filename)

    if img.mode in "RGBA":
        # img_final = np.array(img)
        print(img.mode)
        img.save(save_filename, 'PNG', quality=95)
        return

    img.save(save_filename, file_format_result)


def read_values_for_watermark():
    """Read width and height for watermark mentioned by the user"""
    width_result = width_entry.get()
    height_result = height_entry.get()
    if width_result == '':
        width_result = 100
    else:
        try:
            width_result = int(width_result)
            if width_result < 0 or width_result > 600:
                error_label['text'] = "Invalid Height"
                return
        except ValueError:
            error_label['text'] = "Invalid Width"
            return

    if height_result == '':
        height_result = 100
    else:
        try:
            height_result = int(height_result)
            if height_result < 0 or height_result > 600:
                error_label['text'] = "Invalid Height"
                return
        except ValueError:
            error_label['text'] = "Invalid Height"
            return
    return width_result, height_result


def get_file_format():
    """Get the file format selected by the user"""
    file_format_result = menu.get()

    if file_format_result == 'Select File Format':
        file_format_result = 'JPEG'

    return file_format_result


def get_transparency():
    """Get the transparency selected by the user"""
    transparency_result = transparency_entry.get()

    if transparency_result == '':
        transparency_result = 50
    else:
        try:
            transparency_result = int(transparency_result)
            if transparency_result < 0 or transparency_result > 100:
                error_label['text'] = "Invalid Transparency"
                return
        except ValueError:
            error_label['text'] = "Invalid Transparency"
            return

    return transparency_result


def get_location_result():
    """Get the location selected by the user"""
    location_result = location_dropdown.get()

    if location_result == '':
        location_result = None
    else:
        try:
            open(location_result, 'r')
        except FileNotFoundError:
            error_label['text'] = "Invalid Location"
            return
        except PermissionError:
            pass

    return location_result


def fetch_file_name(mode='s'):
    """Fetch the file name/names specified by the user"""
    f_types = [('JPG files', '*.jpg'),
               ('PNG files', '*.png'),
               ('Image Files', '*.jpeg')]
    if mode == 's':
        filename = filedialog.askopenfilename(filetypes=f_types)
        print(filename)
    else:
        filename = filedialog.askopenfilenames(filetypes=f_types)
        print([x for x in filename])
    return filename


def non_watermark_images():
    """Start the process of adding watermark"""
    global filenames_watermark
    filenames_watermark = fetch_file_name(mode='m')
    if len(filenames_watermark) == 0:
        error_label['text'] = "No file selected"
        return


def add_watermark_to_images():
    """Add watermark to the image"""
    global filenames_watermark
    if isinstance(filenames_watermark, str):
        error_label['text'] = "Upload Images first"
        return

    file_format_result = get_file_format()
    location_result = get_location_result()

    for x in filenames_watermark:
        uploaded_image = Image.open(x)
        if isinstance(watermark, Image.Image):
            print("Image is valid")
            width, height = uploaded_image.size
            width_watermark, height_watermark = watermark.size
            width -= width_watermark
            height -= height_watermark
            if watermark.mode == 'RGBA':
                uploaded_image = uploaded_image.convert('RGBA')
                print('Mode', uploaded_image.mode)
            uploaded_image.paste(watermark, (width, height))

            save_file(uploaded_image, 'logos', x, location_result, file_format_result)
        else:
            error_label['text'] = "Upload Watermark first"
        uploaded_image.close()


def upload_watermark():
    """Upload the watermark"""
    global filename_edit_watermark
    filename_edit_watermark = fetch_file_name()


def edit_watermark():
    """Edit the watermark"""
    global filename_edit_watermark, watermark

    if filename_edit_watermark == "":
        error_label['text'] = "Upload Watermark first"
        return

    width, height = read_values_for_watermark()

    if width is None:
        return

    size = (width, height)
    print(size)

    try:
        watermark = Image.open(filename_edit_watermark)
        print(type(watermark))

        # Image to array
        # img_arr = np.array(watermark, dtype='int32')
        # print(img_arr)

        # Resizing
        watermark.thumbnail(size, Image.LANCZOS)
        print(watermark.size)

        location_result = get_location_result()
        transparency_result = get_transparency()
        file_format_result = get_file_format()

        # Transparent Image
        value = int((transparency_result / 100) * 255)
        print(value)
        watermark.putalpha(value)

        save_file(watermark, 'watermark', filename_edit_watermark, location_result, file_format_result)
    except AttributeError:
        print('Ent')
        error_label['text'] = "Upload a valid Image"


window.mainloop()  # Keep the window open
