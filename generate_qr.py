import qrcode

url = "http://127.0.0.1:5000/"

img = qrcode.make(url)
img.save("test_qr.png")

print("Test QR created")