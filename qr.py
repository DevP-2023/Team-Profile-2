import qrcode

# Website link
url = "https://electricity-load-forecasting-teamprofile.vercel.app/"

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Generate image
img = qr.make_image(fill_color="black", back_color="white")

# Save QR code
img.save("website_qr1.png")

print("QR code generated and saved as website_qr.png")
