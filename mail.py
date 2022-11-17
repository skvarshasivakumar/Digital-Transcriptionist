import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
body = '''Hello. This is Varsha S K from Team Tech Zombies herewith we have  attached the
notes that you recorded using our Automated Notes Maker. Keep using our GUI and finally hearty Thanks!
'''
sender = 'skvarshasivakumar@gmail.com'
password = 'aqrqbfjbjrqbkapb'
x=input("ADMIN please do enter receiver mail id:")
receiver = x
 
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'This email has an attachment, a pdf file'
 
message.attach(MIMEText(body, 'plain'))
 
pdfname = 'notes.pdf'
 
binary_pdf = open(pdfname, 'rb')
 
payload = MIMEBase('application', 'octate-stream', Name=pdfname)
payload.set_payload((binary_pdf).read())
 
encoders.encode_base64(payload)

payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload)
 
session = smtplib.SMTP('smtp.gmail.com', 587)
 
session.starttls()
 
session.login(sender, password)
 
text = message.as_string()
session.sendmail(sender, receiver, text)
session.quit()
print('Mail has been successfully Sent.Thanks for using our GUI!')
