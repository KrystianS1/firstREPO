import qrcode

# Adres URL strony internetowej, dla której chcemy wygenerować kod QR
url = ""

# Tworzymy obiekt QRCode
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Dodajemy do obiektu QRCode adres URL strony internetowej
qr.add_data(url)

# Generujemy kod QR w formie obrazka PNG
img = qr.make_image(fill_color="black", back_color="white")

# Zapisujemy kod QR do pliku PNG
img.save("kod-qr.png")
