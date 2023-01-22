import qrcode

def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save("qr_code.png")

if __name__ == '__main__':
    url = f"http://{socket.gethostbyname(socket.gethostname())}:8000"
    generate_qr(url)
