import pyqrcode 
from pyqrcode import QRCode
s="https://www.youtube.com/channel/UCXZIz_zTs-yaaN99WrfwuuA"
url=pyqrcode.create(s)
url.svg("@tech.art2205.svg",scale=10)