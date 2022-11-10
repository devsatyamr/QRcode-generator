import pyqrcode
import png
from pyqrcode import QRCode

s = input(str("Enter your text behind QR: "))

url = pyqrcode.create(s)

url.svg("myqr.svg", scale = 8)
url.png("myqr.png", scale = 6)

