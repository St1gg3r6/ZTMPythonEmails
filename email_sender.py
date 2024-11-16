import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


pwd = input("Password: ").strip()
msg_from = 'stephenusher@me.com'
msg_to = 'steveusher34@btinternet.com'


def send_email1():
    email = EmailMessage()
    email['from'] = msg_from
    email['to'] = msg_to
    email['subject'] = 'Test Python Email Sender'

    email.set_content("I am testing sending emails in Python.")

    send_msg(email)


def send_email2():
    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['from'] = msg_from
    email['to'] = msg_to
    email['subject'] = 'Test Python HTML Message'

    email.set_content(html.substitute(who = 'Steve'), 'html')

    send_msg(email)


def send_msg(msg):
    with smtplib.SMTP(host='smtp.mail.me.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('stephenusher@me.com', pwd)
        smtp.send_message(msg)
        print("Email sent.")


if __name__ == '__main__':
    send_email2()