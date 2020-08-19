from pyzbar import pyzbar
import argparse
import cv2
from pyfiglet import Figlet

custom_fig = Figlet(font='standard')

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

qrcodes = pyzbar.decode(image)

for qrcode in qrcodes:

	(x, y, w, h) = qrcode.rect
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

	qrcodeData = qrcode.data.decode("utf-8")
	qrcodeType = qrcode.type


	qrtrim = qrcodeData[:40]
	leftqr = qrcodeData.replace(qrtrim, '')
	lasttext = qrtrim + "\n" + leftqr
	text = "{} ({})".format(lasttext, qrcodeType)
	y0, dy = 40, 13
	for i, line in enumerate(text.split('\n')):
		y = y0 + i*dy
		cv2.putText(image, line, (40, y - 30),
		            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)


print("[OUTPUT] Found {} QR code : {}".format(qrcodeType, text))
print(custom_fig.renderText('Done!'))

cv2.imshow("Image", image)
cv2.waitKey(0)
