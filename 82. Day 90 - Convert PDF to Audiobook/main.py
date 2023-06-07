import os
from tkinter import filedialog

from PyPDF2 import PdfReader
from gtts import gTTS

filenames = []

while len(filenames) == 0:
    f_types = [('PDF files', '*.pdf')]

    filenames = filedialog.askopenfilenames(filetypes=f_types)

    print("No files selected")

for filename in filenames:
    # Open the PDF file in read-binary mode
    # Open the PDF file in read-binary mode
    with open(filename, 'rb') as file:

        # Create a PdfReader object
        reader = PdfReader(file)

        # Iterate through each page
        for page in reader.pages:
            # Extract the text from the page
            text = page.extract_text()
            print(text)

    temp1 = filename.split('/')[-1].split('.')[-2]
    try:
        open('/'.join(filename.split("/")[:-1]) + "/tts_pdf/", 'r')
    except FileNotFoundError:
        os.mkdir('/'.join(filename.split("/")[:-1]) + "/tts_pdf/")
    except PermissionError:
        pass

    save_filename = '/'.join(
        filename.split("/")[:-1]) + "/tts_pdf/" + temp1 + "tts.mp3"
    print(save_filename)

    tts = gTTS(text=text)
    tts.save(save_filename)
