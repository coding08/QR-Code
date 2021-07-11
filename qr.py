import pyqrcode
import png
from pyqrcode import QRCode
s= Enter URL /NUMBER
num=pyqrcode.create(s)
num.svg("myqr.svg",scale=8)
num.png("myqr.png",scale=8)
