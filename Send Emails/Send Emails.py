import smtplib
import imghdr
from email.message import EmailMessage

email_id = 'tatiyaparam@gmail.com'
password = '420420007'

# to add the text part
msg = EmailMessage()
msg['Subject'] = 'Checkout a simple PIC'
msg['From'] = email_id
msg['To'] = 'paramtatiya@gmail.com'  # to send mail to multiple contacts create a list of emails and enter
# ', '.join(name of the list variable)
msg.set_content("Image has been Attached!!!!")

# to add images
# TO ADD MULTIPLE FILES ADD THEM IN A LIST AND USE FOR LOOP TO READ IT ONE BY ONE
files = ['2.pdf', '1.jpg']
for file in files:
    img = open(file, 'rb')
    file_data = img.read()
    file_name = img.name
# file_type = imghdr.what(img.name)   it will give the name of the file to the receiver
# i'll show you the type of the file
# print(file_type)

    msg.add_attachment(file_data, maintype='image', subtype='octet-stream', filename=file_name)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email_id, password)
server.send_message(msg)
