
import qrcode

from pyscript.web import page

from pyscript import display


def qrcodegenerator(event):
    try:

        data = page["#url"].value
        img = qrcode.make(data)

        display (img, target="qrcode-box", append=False)
    except ValueError:
        display ("Error", target="qrcode-box")