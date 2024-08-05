import qrcode

def generate_qr_code(link, filename):
    # Create a QR code object with the provided link
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code object
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the specified filename
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

if __name__ == "__main__":
    # Replace the link and filename with your desired values
    web_link = "http://melodychirinos.notion.site"
    output_filename = "Portfolio_qrcode.png"

    generate_qr_code(web_link, output_filename)
