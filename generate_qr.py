import qrcode

url = "https://scan2service.onrender.com"

img = qrcode.make(url)
img.save("scan2service_qr.png")

print("QR READY")