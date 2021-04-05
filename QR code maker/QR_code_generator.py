import qrcode
import image

qr = qrcode.QRCode(
    version=15,  # 15 means the version of the qr code high the number bigger the code image and complicated pictures
    box_size=10,  # size of the box where qr code will be displayed
    border=5  # it is the white part of the image -- border in all 4 sides with white color
)

# a path of a random url
# if you don't want to redirect and create qr for normal text then just write it in double quotes
# EXAMPLE data = "Hello Everyone"
data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("test.png")