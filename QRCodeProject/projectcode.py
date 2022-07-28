import qrcode

#Variable d stores the encoded data 

d = " This is a QRCode message "

img = qrcode.make(d)

img.save('image.png')