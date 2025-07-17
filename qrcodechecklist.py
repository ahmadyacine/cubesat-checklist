
import qrcode

url = "https://ahmadyacine.github.io/cubesat-checklist/"
qr = qrcode.make(url)
qr.save("cubesat_site_qr.png")
