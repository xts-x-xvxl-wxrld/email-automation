import smtplib
from my_email_logins import login_email, login_password
from reciever_add import reciever1

server_name = 'smtp.mail.ru'
port = 465

smtp_port = smtplib.SMTP_SSL(server_name, port)

smtp_port.login(login_email, login_password)

sub = 'Hi, this is a test'
bod = 'This body is amazing'
message = f"Subject: {sub} \n \n {bod}"

recievers_list = [reciever1]
smtp_port.sendmail(login_email, recievers_list, message)

print('email sent')

smtp_port.quit()
