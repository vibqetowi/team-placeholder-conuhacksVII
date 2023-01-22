import qrcode
import urllib.request
from json_reader import JSONFileReader



class QR_Code:
    def __init__(self, data):
        self.data = data

    def generate_qr_code(self, file_path):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(self.data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(file_path)



# Example usage
file_reader = JSONFileReader('vault.json')
json_str = file_reader.read_file()
qr_code = QR_Code(json_str)
qr_code.generate_qr_code("qr_code.png")
print(json_str)


