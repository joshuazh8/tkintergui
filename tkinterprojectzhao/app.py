#added attribute: added a copy button so that when pressed, text will get copied onto clipboard for pasting.
# Zhaohua Zhang 132
# APCSP P1
#2/2/23

#added attribute: added a copy button so that when pressed, text will get copied onto clipboard for pasting.
# Zhaohua Zhang 132
# APCSP P1
#2/2/23

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()

        #text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        # copy text button
        def copy_text():
            text_box.tag_add("sel", "1.0", "end")
            text_box.event_generate("<<Copy>>")

        copy_text_btn = tk.Button(root, text="Copy Text", command=lambda:copy_text(), font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
        copy_text_btn.grid(column=2, row=3)

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()

