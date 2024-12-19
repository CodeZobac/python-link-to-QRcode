import qrcode
import qrcode.image.svg


def generate_qr(file_type, path_website, fill_color, back_color, name):
    """
    Generates a QR code image based on the provided parameters and saves it to a file.
    Args:
        file_type (str): The type of the output file (e.g., 'svg' or 'png').
        path_website (str): The website URL or data to encode into the QR code.
        fill_color (str): The color of the QR code modules. Defaults to 'black' if empty.
        back_color (str): The background color of the QR code. Defaults to 'white' if empty.
        name (str): The name of the output file (without extension).
    Raises:
        ValueError: If 'file_type' is not 'svg' or 'png', or if 'name' is left blank.
    Returns:
        None: The function saves the generated QR code image to a file.
    """
    factory = qrcode.image.svg.SvgPathImage

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=30,
        border=1,
    )

    qr.add_data(path_website)
    qr.make(fit=True)

    if fill_color == "":
        fill_color = "black"
    if back_color == "":
        back_color = "white"

    name = name
    file_type = file_type
    if name == "":
        name = "QRcode"
    while file_type != "svg" and file_type != "png":
        file_type = input("Please enter a valid file type(PNG or SVG): ").lower()

    if file_type == "svg":
        img = qr.make_image(
            fill_color=fill_color, back_color=back_color, image_factory=factory
        )
    else:
        try:
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
        except Exception as e:
            print("\n\nAn error occurred. Please enter a valid color.")
            fill_color = input(
                "Enter the fill color of the QRcode(Press enter for black): "
            ).lower()
            back_color = input(
                "Enter the background color of the QRcode(Press enter for white): "
            ).lower()
            try:
                img = qr.make_image(fill_color=fill_color, back_color=back_color)
            except Exception as e:
                print(
                    f"\n\nAn error occurred, please try again with VALID colors ¯\_(ツ)_/¯: {e}"
                )
                return generate_qr(
                    file_type, path_website, fill_color, back_color, name
                )

    if img:
        return img.save(f"{name}.{file_type}")


file_type = input(
    "Welcome to the QRcode generator. Enter the file type you want to generate(Chose between SVG and PNG): "
).lower()
path_website = input("Enter the website URL: ")
fill_color = input(
    "Enter the fill color of the QRcode(Press enter for black): "
).lower()
back_color = input(
    "Enter the background color of the QRcode(Press enter for white): "
).lower()
name = input("Enter the name of the QRcode file: ")

generate_qr(file_type, path_website, fill_color, back_color, name)
