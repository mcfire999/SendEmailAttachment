import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr = "musicmaninthesky@gmail.com"
toaddr = "samcarr999@gmail.com" 
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Please find the attachment"
body = "HI" 
msg.attach(MIMEText(body, 'plain')) 
filename = "myfile.txt"
#dt = str(datetime.datetime.now())
attachment = open("F:\\D\\OneDrive\\Python\\Spyder\\myfile.txt", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(part) 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "pokemon16")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

