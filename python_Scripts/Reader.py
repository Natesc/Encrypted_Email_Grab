import imaplib
import email

def readmail(from_email, from_pwd, smtp_server, coming):
    tries = 0

    mail = imaplib.IMAP4_SSL(smtp_server) # Define server
    mail.login(from_email, from_pwd) # Login to Server
    mail.select('Inbox') # Select Inbox

    result, data = mail.search(None, 'FROM', coming)
    mail_ids = data[0]
    id_list = mail_ids.split()

    while len(id_list) <= 0:
        if tries < 2:
            tries += 1
            coming = input('No Messages Try Again: ')
            result, data = mail.search(None, 'FROM', coming)
            mail_ids = data[0]
            id_list = mail_ids.split()
        else:
            return


    latest_email_id = id_list[-1]
    result, data = mail.fetch(latest_email_id, '(RFC822)')

    decoded = data[0][1].decode()

    msg = email.message_from_string(decoded)
    
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            string = (part.get_payload())
            x = string.split()
            mail.close()
            mail.logout()
            return x