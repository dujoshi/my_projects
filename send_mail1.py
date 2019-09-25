

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_email(to_add, cc_add, sub, msg_body):
    """
     #this is by using full python smtp lib
     #the other way is to do by using linux sendmail program
     # that method is available in send_mail2.py 
     # send_mail2.py. is also having method to send a report by extracting  important things from that. 
    """
    msg = MIMEMultipart('alternative')
    from_add = 'abcd@xyz.com' #this is from where the mail will come
    msg['Subject'] = sub
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Cc'] = cc_add
    part2 = MIMEText(msg_body, 'html')
    msg.attach(part2)

    receps = to_add.split(",") + cc_add.split(",")

    server = smtplib.SMTP('email.xyz.com') # we need to use some smtp server
    server.sendmail( from_add, receps, msg.as_string())
    server.quit()

to_add='dujoshi@xyz.com'
cc_add='dujoshi@xyz.com'
sub='hi this is test mail'
send_email(to_add, cc_add, sub, 'hi')
