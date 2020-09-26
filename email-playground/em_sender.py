# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage



email = EmailMessage()
email['from'] = 'Brice donald'
email['to'] = 'a_vrv@list.ru'
email['subject'] = 'you won 1,000,000 dollars!'
email.set_content('I am a python dev')

with smtplib.SMTP(host='smtp.mail.yahoo.com', port= 465) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('a_b_e_l_237@yahoo.com','')
	smtp.send_message(email)
	print('all good boss!')
