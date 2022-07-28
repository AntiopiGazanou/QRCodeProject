from pyzbar.pyzbar import decode

i = Image.open("/Users/Antiopi/Desktop/QRCodeProject/image.png")

result = decode(i)

print(result)