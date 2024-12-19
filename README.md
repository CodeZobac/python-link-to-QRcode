# Python Link to QR Code

A simple Python script that converts a URL into a QR code image.

## Features

- Convert any URL into a QR code
- Save the QR code as an image file(SVG or PNG)
- Easy to use command-line interface

## Requirements

- Python ^3.12(Or change the python version on the pyproject.toml file)
- [Poetry](https://python-poetry.org/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/CodeZobac/python-link-to-QRcode.git
    ```

2. Navigate to the project directory:

    ```bash
    cd python-link-to-QRcode
    ```

3. Install the dependencies using Poetry:

    ```bash
    poetry install
    ```

4. Activate the virtual environment:

    ```bash
    poetry shell
    ```

## Usage

Run the script and follow the prompts:

```bash
python main.py
```

Alternatively, run the script without activating the virtual environment:

```bash
poetry run python main.py
```

Example Usage:

```bash
$ python main.py
Enter the URL: https://www.example.com
QR code has been generated and saved as qrcode.png
```

## License

This project is licensed under the MIT License.
