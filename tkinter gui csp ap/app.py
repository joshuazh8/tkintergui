//added an image opener using pyIMG
from Tkinter import*
import PyPDF2
from PIL import Image, ImageTk
from tkinter import filedialog
from PIL import Image
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
instructions = tk.Label(root, text="Open a PDF document or an image to extract its content", font="Calibri")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("wait...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
   
        #text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Click Here to Open Files")

#extracting image gui         
def extract_images():
    # open file dialog
    filepath = filedialog.askopenfilename()
    
    # use pil to open selected path
    with Image.open(filepath) as im:
        # render image frames
        for i, frame in enumerate(ImageSequence.Iterator(im)):
            # seperate the file frames
            frame.save(f"frame{i}.png")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Calibri", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Click Here to Open File")
browse_btn.grid(column=1, row=2)

#browseImage button
browseImage_text = tk.StringVar()
browseImage_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Calibri", bg="#20bebe", fg="white", height=2, width=15)
browseImage_text.set("Click Here to Open File")
browseImage_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
