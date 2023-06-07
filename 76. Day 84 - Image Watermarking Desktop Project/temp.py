from tkinter import filedialog

f_types = [('PDF files', '*.pdf')]

filename = filedialog.askopenfilenames(filetypes=f_types)
