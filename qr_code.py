import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qr():
    # Get the text from the input field
    data = input_field.get()
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    # Add the data to the QR code object
    qr.add_data(data)
    qr.make(fit=True)
    # Create an image from the QR code object
    img = qr.make_image(fill_color="black", back_color="white")
    # Save the image to a file
    img.save("qr_code.png")
    root.filename = filedialog.asksaveasfilename(initialdir = "./", title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
    img.save(root.filename)
    input_field.delete(0,'end')
    generate_button.config(state='disable')

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create a label for the input field
label = tk.Label(root, text="Enter text:")
label.pack()

# Create the input field
input_field = tk.Entry(root)
input_field.pack()

# Create the generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()
generate_button.config(state='disable')

input_field.bind("<Key>",lambda e: generate_button.config(state='active') if input_field.get() else generate_button.config(state='disable'))

# Run the main loop
root.mainloop()
