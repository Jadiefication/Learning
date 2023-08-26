import qrcode, os, pickle
file_name = "qr.png"
text = input("Please enter input: ")
question = input("Do you wish to encode the text into a QR code? (y/n): ")
if question == "y":
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
elif question == "n":
    text2 = input("Do you have a qr code to decode? (y/n): ")
    if text2 == "y":
        location = input("Please enter the location of the qr code: ")
        if os.path.exists(location):
            print(location)
            confirmation = input("Do you wish to decode the qr code? (y/n): ")
            if confirmation == "y":
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(text)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                img.save(location)
                print("QR code successfully decoded!")
            elif confirmation == "n":
                print("QR code successfully non-decoded!")
            else:
                print("Invalid input!")
        else:
            print("Qr code not found!")
    elif text2 == "n":
        print("No qr code to decode!")
    else:
        print("Invalid input!")
else:
    print("Invalid input!")