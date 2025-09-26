# 🔗 QR Code Generator

A simple, elegant Python application that transforms any URL or text into a QR code! ✨

## 🚀 Features

- **Easy to Use**: Just run the script and enter your link - that's it! 
- **Automatic Timestamping**: Each QR code is saved with a unique timestamp filename
- **High Quality Output**: Generates crisp PNG images perfect for sharing

## 📋 Requirements

Before you start generating awesome QR codes, make sure you have:

- Python 3.6 or higher 🐍
- Required packages (see installation below)

## 🛠️ Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/SAFAL-TIWARI/qr-code
   cd "Qr code"
   ```

2. **Install required packages**
   ```bash
   pip install qrcode[pil]
   ```
   
   This installs:
   - `qrcode`: The main QR code generation library
   - `Pillow (PIL)`: For image processing and saving

## 🎯 Usage

Running the QR Code Generator is super simple:

```bash
python qr-code.py
```

Then just follow the prompt:
```
Enter the link you want generate QR code: https://example.com
```

**Boom!** 💥 Your QR code will be generated and saved as `qr_code_DDMMYYYY_HHMMSS.png`

<b><div align="center" >Made with ❤️ and Python</div></b>
