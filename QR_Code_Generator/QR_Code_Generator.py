import pyqrcode
import png
link = "https://theinsightfulcoder.com"
qr_code = pyqrcode.create(link)
qr_code.png("The Insightful Coder.png", scale=5)