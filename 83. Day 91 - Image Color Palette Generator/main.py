import os
import sys

import numpy as np
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, flash

# Get the absolute path to the directory containing the executable file
# base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

# Set the template and static directories relative to the base path
template_dir = os.path.join(base_path, 'templates')
static_dir = os.path.join(base_path, 'static')

all_colors_count = []
files = []


def top_ten_colors(file):
    print(file.filename)
    print(file.mimetype)
    image = Image.open(file)
    image_array = np.asarray(image)

    rgb_values = image_array.reshape(-1, image_array.shape[-1])
    unique_colors, color_counts = np.unique(rgb_values, axis=0, return_counts=True)
    colors_count = {tuple(k): v for k, v in zip(unique_colors, color_counts)}
    colors_count = dict(sorted(colors_count.items(), key=lambda x: x[1], reverse=True)[:10])
    if (file, colors_count) not in all_colors_count:
        all_colors_count.append((file.filename, colors_count))


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Set the template directory path for Flask
app.template_folder = template_dir

# Set the template directory path for Flask
app.static_folder = static_dir

print(template_dir)
print(static_dir)
print(base_path)

@app.route('/')
def home():
    global all_colors_count
    print(len(all_colors_count))
    return render_template('index.html', all_items=all_colors_count)


@app.route('/add_files', methods=['GET', 'POST'])
def add_files():
    global files
    if request.method == 'POST':
        temp_files = request.files.getlist('add_file')
        print(temp_files)
        print(len(temp_files))
        if len(files) == 0 or files[0].filename == '':
            flash('No files selected!')
            return redirect(url_for('home'))
        files.extend(temp_files)
    return redirect(url_for('home'))


@app.route('/result', methods=['GET', 'POST'])
def result():
    global files, all_colors_count
    if request.method == 'POST':
        files = request.files.getlist('files')
        if len(files) == 0 or files[0].filename == '':
            flash('No files selected!')
            return redirect(url_for('home'))
        for f in files:
            print(f)
            f.save('static/images/' + f.filename)
            top_ten_colors(f)
            if len(all_colors_count) > 0:
                print(all_colors_count[-1])
        flash('File(s) successfully uploaded!')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
