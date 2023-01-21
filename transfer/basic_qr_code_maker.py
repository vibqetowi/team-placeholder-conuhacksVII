# Importing library
import qrcode
from os import path

if __name__ == "__main__":
    
    # Data to be encoded
    data = input("paste string to encode: ")
    # Encoding data using make() function

    img = qrcode.make(data)
    # Saving as an image file
    img.save('specify directory here')

    print("done")