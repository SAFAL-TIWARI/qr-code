import qrcode
from PIL import Image
from datetime import datetime

def generate_qr_code():
    # Get the link from user input
    link = input("Enter the link you want generate QR code: ")

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size
    )

    # Add data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image with timestamp
    # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    filename = f"qr_code_{timestamp}.png"
    img.save(filename)

    print(f"QR code generated successfully and saved as '{filename}'")
    print(f"QR code contains: {link}")

if __name__ == "__main__":
    generate_qr_code()
